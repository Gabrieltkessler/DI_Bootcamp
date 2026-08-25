"""
orchestrator.py
----------------
The MCP client + planning loop for Smart Data Scout.

Responsibilities:
  1. Spawn and connect to every server in mcp_config.json (stdio).
  2. Discover tools from each server, prefix them so names stay
     unique, and convert their JSON schemas into the format Ollama's
     tool-calling API expects.
  3. Run a plan -> act -> observe loop: ask the LLM what to do next,
     execute the chosen tool against the right server, feed the
     result back, repeat until the LLM gives a final answer.
  4. Handle errors with retries/fallback, and log every tool call.

This file has no Streamlit/UI code in it on purpose -- app.py just
drives this class. That makes it easy to also run from a plain CLI
script or tests.
"""
import asyncio
import json
import logging
import os
import time
import httpx
from contextlib import AsyncExitStack
from dataclasses import dataclass, field
from typing import Any, AsyncIterator, Optional

from dotenv import load_dotenv
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from ollama import AsyncClient as OllamaClient

load_dotenv()

# ---------------------------------------------------------------- config --
DATA_DIR = os.environ.get("DATA_DIR", "./data")
OLLAMA_HOST = os.environ.get("OLLAMA_HOST", "http://localhost:11434")
OLLAMA_MODEL = os.environ.get("OLLAMA_MODEL", "llama3.1")
LLM_PROVIDER = os.environ.get("LLM_PROVIDER", "ollama").lower()
GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")
GROQ_MODEL = os.environ.get("GROQ_MODEL", "llama-3.1-70b-versatile")
MAX_STEPS = int(os.environ.get("MAX_STEPS", 8))
MAX_RETRIES = int(os.environ.get("MAX_RETRIES", 2))
RETRY_BACKOFF = float(os.environ.get("RETRY_BACKOFF_SECONDS", 1.5))
LOG_FILE = os.environ.get("LOG_FILE", "./logs/session.log")
LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")

os.makedirs(os.path.dirname(LOG_FILE) or ".", exist_ok=True)
os.makedirs(DATA_DIR, exist_ok=True)

logging.basicConfig(
    level=LOG_LEVEL,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[logging.FileHandler(LOG_FILE), logging.StreamHandler()],
)
logger = logging.getLogger("smart_data_scout")


def _truncate(obj: Any, limit: int = 400) -> str:
    """Summarize a value for logging so we never dump huge payloads
    (or secrets) into the log file."""
    s = obj if isinstance(obj, str) else json.dumps(obj, default=str)
    return s if len(s) <= limit else s[:limit] + f"...<{len(s) - limit} more chars>"


@dataclass
class StepEvent:
    """One observable event, yielded to the UI as the loop runs."""
    kind: str  # "plan" | "tool_call" | "tool_result" | "error" | "final"
    detail: str
    server: Optional[str] = None
    tool: Optional[str] = None
    meta: dict = field(default_factory=dict)


class Orchestrator:
    def __init__(self, config_path: str = "mcp_config.json"):
        self.config_path = config_path
        self.exit_stack = AsyncExitStack()
        self.sessions: dict[str, ClientSession] = {}
        self.tool_owner: dict[str, str] = {}  # prefixed_name -> server key
        self.ollama_tools: list[dict] = []
        self.ollama = OllamaClient(host=OLLAMA_HOST)

    # ------------------------------------------------------------ setup --
    async def connect_all(self) -> AsyncIterator[StepEvent]:
        with open(self.config_path) as f:
            config = json.load(f)

        for server_key, spec in config.items():
            yield StepEvent("plan", f"Connecting to '{server_key}' server...", server=server_key)
            params = StdioServerParameters(
                command=spec["command"],
                args=spec.get("args", []),
                env=os.environ.copy(),
            )
            try:
                read, write = await self.exit_stack.enter_async_context(stdio_client(params))
                session = await self.exit_stack.enter_async_context(ClientSession(read, write))
                await session.initialize()
                self.sessions[server_key] = session

                tools_resp = await session.list_tools()
                for tool in tools_resp.tools:
                    prefixed = f"{server_key}__{tool.name}"
                    self.tool_owner[prefixed] = server_key
                    schema = (
                        getattr(tool, "inputSchema", None) 
                        or getattr(tool, "input_schema", None) 
                        or {"type": "object", "properties": {}}
                    )

                    self.ollama_tools.append({
                        "type": "function",
                        "function": {
                            "name": prefixed,
                            "description": tool.description or "",
                            "parameters": schema,
                        },
                    })
                logger.info("Connected to %s (%d tools)", server_key, len(tools_resp.tools))
                yield StepEvent(
                    "plan",
                    f"'{server_key}' ready with {len(tools_resp.tools)} tool(s): "
                    + ", ".join(t.name for t in tools_resp.tools),
                    server=server_key,
                )
            except Exception as e:
                logger.error("Failed to connect to %s: %s", server_key, e)
                yield StepEvent("error", f"Could not start '{server_key}': {e}", server=server_key)

    async def aclose(self):
        await self.exit_stack.aclose()

    # --------------------------------------------------------- execution --
    async def _call_tool_with_retry(self, prefixed_name: str, args: dict) -> tuple[bool, str]:
        server_key = self.tool_owner.get(prefixed_name)
        if server_key is None:
            return False, f"Unknown tool '{prefixed_name}'"

        _, tool_name = prefixed_name.split("__", 1)
        session = self.sessions[server_key]

        attempt = 0
        while True:
            attempt += 1
            try:
                start = time.time()
                result = await asyncio.wait_for(
                    session.call_tool(tool_name, args), timeout=30.0
                )
                elapsed = time.time() - start
                text = "\n".join(
                    block.text for block in result.content if hasattr(block, "text")
                )
                logger.info(
                    "tool_call server=%s tool=%s args=%s -> ok in %.2fs result=%s",
                    server_key, tool_name, _truncate(args), elapsed, _truncate(text),
                )
                return True, text
            except (asyncio.TimeoutError, Exception) as e:
                logger.warning(
                    "tool_call FAILED (attempt %d/%d) server=%s tool=%s args=%s err=%s",
                    attempt, MAX_RETRIES + 1, server_key, tool_name, _truncate(args), e,
                )
                if attempt > MAX_RETRIES:
                    return False, f"Tool '{tool_name}' failed after {attempt} attempts: {e}"
                await asyncio.sleep(RETRY_BACKOFF * attempt)

    # -------------------------------------------------------------- loop --
    async def run_goal(self, goal: str) -> AsyncIterator[StepEvent]:
        """The plan -> act -> observe loop. Yields StepEvents as it goes
        and the last event is always kind='final'."""
        system_prompt = (
    "You are an AI data scout running on Windows.\n"
    "Your workspace directory is '.' (which maps to your local data folder).\n\n"
    "CRITICAL PATH & TOOL RULES:\n"
    "- NEVER use absolute paths like '/home/user/data' or '/data'.\n"
    "- ALWAYS start file searches using path '.' with 'filesystem__list_directory'.\n"
    "- Available insights tools are ONLY: 'insights__describe_csv', 'insights__correlate_columns', 'insights__detect_outliers', and 'insights__write_markdown_report'.\n"
    "- There is NO tool called 'insights__read_csv'. To analyze a CSV, use 'insights__describe_csv' with parameter {'file_path': 'sample_sales.csv'}.\n\n"
    "Execution rule: Call ONE tool per turn until you have gathered all needed data, then write a clear plain-text answer without tool calls."
)
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": goal},
        ]

        for step in range(1, MAX_STEPS + 1):
            active_model = GROQ_MODEL if LLM_PROVIDER == "groq" else OLLAMA_MODEL
            yield StepEvent("plan", f"Step {step}: asking {active_model} ({LLM_PROVIDER}) what to do next...")
            
            try:
                if LLM_PROVIDER == "groq":
                    async with httpx.AsyncClient(timeout=60.0) as client:
                        resp = await client.post(
                            "https://api.groq.com/openai/v1/chat/completions",
                            headers={
                                "Authorization": f"Bearer {GROQ_API_KEY}",
                                "Content-Type": "application/json",
                            },
                            json={
                                "model": GROQ_MODEL,
                                "messages": messages,
                                "tools": self.ollama_tools,
                            },
                        )
                        resp.raise_for_status()
                        groq_data = resp.json()
                        groq_msg = groq_data["choices"][0]["message"]
                        
                        tool_calls_formatted = []
                        if groq_msg.get("tool_calls"):
                            for tc in groq_msg["tool_calls"]:
                                tool_calls_formatted.append({
                                    "function": {
                                        "name": tc["function"]["name"],
                                        "arguments": tc["function"]["arguments"]
                                    }
                                })
                        msg = {
                            "role": "assistant",
                            "content": groq_msg.get("content") or "",
                            "tool_calls": tool_calls_formatted
                        }
                else:
                    response = await self.ollama.chat(
                        model=OLLAMA_MODEL,
                        messages=messages,
                        tools=self.ollama_tools,
                    )
                    msg = response["message"]
            except Exception as e:
                logger.error("LLM call failed: %s", e)
                yield StepEvent("error", f"LLM call failed: {e}")
                yield StepEvent("final", f"Stopped early: could not reach {LLM_PROVIDER} model ({e}).")
                return

            tool_calls = msg.get("tool_calls") or []

            if not tool_calls:
                final_text = msg.get("content", "").strip() or "(no response)"
                yield StepEvent("final", final_text)
                return

            messages.append(msg)

            for call in tool_calls:
                name = call["function"]["name"]
                args = call["function"].get("arguments") or {}
                if isinstance(args, str):
                    try:
                        args = json.loads(args)
                    except json.JSONDecodeError:
                        args = {}

                yield StepEvent("tool_call", f"Calling {name}({_truncate(args, 150)})",
                                 server=self.tool_owner.get(name), tool=name)

                ok, result_text = await self._call_tool_with_retry(name, args)

                if not ok:
                    yield StepEvent("error", result_text, tool=name)
                    result_text = f"ERROR: {result_text}"
                else:
                    yield StepEvent("tool_result", _truncate(result_text, 300), tool=name)

                messages.append({
                    "role": "tool",
                    "content": result_text,
                })

        yield StepEvent("final", f"Stopped after reaching the {MAX_STEPS}-step limit without a final answer.")


async def _demo():
    """Quick CLI smoke test: python orchestrator.py"""
    orch = Orchestrator()
    async for ev in orch.connect_all():
        print(f"[{ev.kind}] {ev.detail}")
    try:
        async for ev in orch.run_goal(
    "List the files in the directory using path '.'. If you find a CSV file, use the insights tool describe_csv to analyze it."
):
            print(f"[{ev.kind}] {ev.detail}")
    finally:
        await orch.aclose()


if __name__ == "__main__":
    asyncio.run(_demo())
