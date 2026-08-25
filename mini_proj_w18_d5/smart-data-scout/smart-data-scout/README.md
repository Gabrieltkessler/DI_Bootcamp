# Smart Data Scout

An agentic app that composes **two third-party MCP servers** (filesystem,
fetch) with **one custom MCP server** (insights), orchestrated by a
**local Ollama model** that plans and executes tool calls step by step.

## Architecture

```
                ┌────────────────────┐
   Streamlit ── │   orchestrator.py   │
     (app.py)   │  (MCP client + LLM  │
                │     planning loop)   │
                └─────────┬───────────┘
                          │ stdio (spawned subprocesses)
        ┌─────────────────┼─────────────────┐
        │                 │                 │
 ┌─────────────┐   ┌─────────────┐   ┌──────────────┐
 │ filesystem   │   │   fetch     │   │  insights     │
 │ (official,   │   │ (official,  │   │  (yours,      │
 │  npx)        │   │  uvx)       │   │  FastMCP)     │
 │ 3rd-party    │   │ 3rd-party   │   │  describe_csv │
 │              │   │             │   │  correlate    │
 │              │   │             │   │  outliers     │
 │              │   │             │   │  write_report │
 └─────────────┘   └─────────────┘   └──────────────┘
```

The LLM sees the merged tool list from all three servers and decides,
turn by turn, which tool to call next -- nothing is hard-coded.

## Prerequisites

- Python 3.10+
- [Node.js](https://nodejs.org/) (for `npx`, used by the filesystem server)
- [uv](https://docs.astral.sh/uv/) (for `uvx`, used by the fetch server) — `pip install uv`
- [Ollama](https://ollama.com/) installed and running, with a tool-calling
  capable model pulled, e.g.:
  ```bash
  ollama pull llama3.1
  ```

## Setup (clean machine)

```bash
cd smart-data-scout
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env      # adjust OLLAMA_MODEL etc. if needed
ollama serve &             # if not already running
streamlit run app.py
```

That's it — the app spawns the filesystem, fetch, and insights MCP
servers itself on first run (via `npx`/`uvx`/`python`), no separate
terminal windows needed.

## Try it

A sample CSV is included at `data/sample_sales.csv`. Example goals to type
into the app:

- *"List the files in the data directory, then give me summary statistics
  for sample_sales.csv."*
- *"Check if units_sold and revenue are correlated in sample_sales.csv,
  then write a short markdown report of your finding to insights.md."*
- *"Find outliers in the revenue column of sample_sales.csv and write a
  report explaining what you found."*
- *"Fetch https://en.wikipedia.org/wiki/Data_science, save a short summary
  of the intro to summary.md."* (exercises the fetch server)

## How the requirements are met

| Requirement | Where |
|---|---|
| ≥2 third-party MCP servers | `mcp_config.json`: `filesystem`, `fetch` |
| Your own server | `insights_server.py` |
| Local execution | All servers spawned as subprocesses over stdio |
| LLM plans tool order | `orchestrator.run_goal()` — no hard-coded call sequence, model chooses via Ollama tool-calling |
| Error handling | `_call_tool_with_retry()` — timeout + retry with backoff, errors fed back to the LLM as tool results so it can adapt |
| Observability | `logging` to `logs/session.log` (tool name, truncated args/results, timing) + live trace in the Streamlit UI |
| Config | `.env` (`OLLAMA_MODEL`, `OLLAMA_HOST`, retry/step limits) + `mcp_config.json` (server commands) |
| Reproducibility | Single `pip install` + `streamlit run app.py` |

## Swapping in GroqCloud instead of Ollama

The orchestrator only touches Ollama in `orchestrator.py`'s `__init__`
(`self.ollama = OllamaClient(...)`) and the `chat()` call inside
`run_goal()`. To use Groq instead:

1. `pip install groq`
2. Replace the Ollama client with `groq.AsyncGroq(api_key=os.environ["GROQ_API_KEY"])`
3. Groq's `chat.completions.create(..., tools=self.ollama_tools)` uses the
   same OpenAI-style tool schema, so `self.ollama_tools` and the
   tool-call parsing logic need only minor field-name adjustments
   (`response.choices[0].message.tool_calls`).

## Extending

- Add another third-party server: add an entry to `mcp_config.json`,
  nothing else changes — tools are auto-discovered.
- Add your own tools: add `@mcp.tool()` functions to `insights_server.py`.
