"""
app.py
------
Streamlit front-end for Smart Data Scout.

Run with:
    streamlit run app.py
"""
import asyncio

import streamlit as st

from orchestrator import Orchestrator, OLLAMA_MODEL, OLLAMA_HOST

st.set_page_config(page_title="Smart Data Scout", page_icon="🔎", layout="centered")

st.title("🔎 Smart Data Scout")
st.caption(
    "Agentic pipeline: filesystem server + fetch server (third-party MCP) "
    "+ your insights server, orchestrated by an Ollama model."
)

with st.sidebar:
    st.subheader("Config")
    st.write(f"**Model:** `{OLLAMA_MODEL}`")
    st.write(f"**Ollama host:** `{OLLAMA_HOST}`")
    st.write("**Servers:** filesystem, fetch, insights")
    st.caption("Edit `.env` / `mcp_config.json` to change these.")

goal = st.text_area(
    "What should the agent do?",
    placeholder="e.g. Fetch https://example.com/data.csv, save it as sample.csv, "
                "describe its statistics, and write a short markdown report.",
    height=100,
)

run = st.button("Run", type="primary", disabled=not goal.strip())

ICONS = {
    "plan": "🧠",
    "tool_call": "🔧",
    "tool_result": "✅",
    "error": "⚠️",
    "final": "🏁",
}


async def _run_and_render(goal_text: str, log_container, final_container):
    orch = Orchestrator()
    try:
        async for ev in orch.connect_all():
            icon = ICONS.get(ev.kind, "•")
            log_container.write(f"{icon} {ev.detail}")

        async for ev in orch.run_goal(goal_text):
            icon = ICONS.get(ev.kind, "•")
            if ev.kind == "final":
                final_container.markdown(ev.detail)
            else:
                log_container.write(f"{icon} {ev.detail}")
    finally:
        await orch.aclose()


if run:
    st.subheader("Agent trace")
    log_box = st.container(border=True)
    st.subheader("Final answer")
    final_box = st.empty()
    with st.spinner("Running agent..."):
        asyncio.run(_run_and_render(goal, log_box, final_box))
