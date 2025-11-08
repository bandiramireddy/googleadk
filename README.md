# Google ADK — Example Agents Repository

This repository contains a collection of small example apps built with the Google Agent Development Kit (ADK). The goal is to demonstrate common agent design patterns for LLM-based systems, integrations with external toolsets (MCP, BigQuery, search), and practical patterns such as sequential pipelines, parallel analysis, and iterative refinement loops.

This README summarizes the whole project idea, how the samples are organized, how to run them, and next steps for development.

## Project idea (high-level)

- Teach developers how to compose small LLM agents into useful workflows using ADK primitives such as `LlmAgent`, `SequentialAgent`, `ParallelAgent`, and `LoopAgent`.
- Show safe tool integrations: local deterministic tools (Python functions), ADK built-in tools (e.g., web search), managed toolsets (BigQuery), and MCP toolsets for real-time streaming or external services.
- Provide reproducible, runnable examples so readers can try different patterns locally and adapt them to their own use cases.

## Repo layout and what's included

- `agent1/` — a minimal single-agent example (`firstagent.py`).
- `agent1_builtintools/` — LLM agent using ADK built-in tools (google search).
- `agent1_functiontools/` — agent with local Python function tools (weather, arithmetic).
- `agent2_sequentialagent/` — code pipeline (writer -> reviewer -> refactorer) using `SequentialAgent`.
- `agent3_parallelagent/` — parallel investment analyst (sentiment, valuation, risk) using `ParallelAgent`.
- `agent4_loopagent/` — iterative article generation and refinement using `LoopAgent` inside a `SequentialAgent`.
- `agent6_mcptavilysearch/` — MCP toolset integration (Tavily) showing real-time web search.
- `agent7_bigquery/` — BigQuery toolset example (service account configured in code).
- `agent8_mcpselfserver/` — local MCP example (weather via local MCP server).
- `agent9_mcpn8nemail/` — MCP-based email composition/send example.
- `agent9_mcpn8nrag/` — RAG-style agent using MCP to query a vector-store-backed pipeline.
- `requirements.txt`, `pyproject.toml` — dependency manifests.
- Per-agent READMEs: each agent folder now contains a `README.md` describing that example (inputs/outputs, env vars, quick run notes).

## How to run the examples (quick start)

1. Create and activate a Python virtual environment.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

3. Create a `.env` file at the repo root for any keys you need (see the per-agent READMEs for specifics). Example:

```
GEMINI_MODEL=gemini-2.5-flash
TAVILY_API_KEY=tvly-xxxx
# SERVICE_ACCOUNT_PATH=./service-key.json (for BigQuery agent)
```

4. Start the ADK services you need. Common commands:

```powershell
# Start the ADK web UI
adk web --port 9000

# Start the ADK API server (exposes /run and management endpoints)
adk api_server --port 9000
# Allow CORS when embedding: adk api_server --allow_origins="*"
```

5. Use the ADK REST API to run an agent (example):

```powershell
curl -X POST "http://localhost:8000/run" -H "Content-Type: application/json" -d '{"app_name":"agent1","user_id":"u_123","session_id":"s_123","new_message":{"role":"user","parts":[{"text":"Hello from ADK"}]}}'
```

Notes
- On Windows, the bundled `curl` may behave differently in PowerShell; use Postman or another HTTP client if needed.
- Some agents expect external services (MCP endpoints, BigQuery service accounts, or local MCP servers). Ensure those services are running and reachable when you test those agents.

## Per-agent summaries (short)

- `agent1/` — Minimal agent; good for quick sanity checks.
- `agent1_builtintools/` — Shows ADK built-in tool integration (google_search).
- `agent1_functiontools/` — Demonstrates local function tools: `weather_tool` and `addition_tool`.
- `agent2_sequentialagent/` — Code generation pipeline: writer -> reviewer -> refactorer, with state passing via output keys.
- `agent3_parallelagent/` — Investment analyst performing sentiment, valuation, and risk analyses in parallel.
- `agent4_loopagent/` — Iterative article generator with an editor and critic, demonstrating loop termination via a tool.
- `agent6_mcptavilysearch/` — Integrates a remote MCP toolset for streaming web search.
- `agent7_bigquery/` — BigQuery tool integration for SQL queries and data analysis.
- `agent8_mcpselfserver/` — Uses a local MCP server (weather example).
- `agent9_mcpn8nemail/` — Email composition and sending via an MCP toolset.
- `agent9_mcpn8nrag/` — RAG agent using MCP + vector store; enforced behavior when no documents found to avoid hallucination.

## Environment variables & secrets

- Keep secrets out of the repository. Use a `.env` file or your environment provisioning.
- Keys seen in examples:
	- `GEMINI_MODEL` — default LLM model string used in many examples.
	- `TAVILY_API_KEY` — Tavily MCP API key.
	- `SERVICE_ACCOUNT_PATH` or a path to a service account JSON file for BigQuery.
	- MCP endpoint URLs in several examples (update in-file or via env vars if you adapt the code).

Add a `.env.example` file (not included by default) showing required keys without values.

## Tests and smoke-checks (recommended)

- Add a small smoke-test script that:
	- Posts a sample `/run` request to the ADK server for `agent1` or `agent3_parallelagent`.
	- Validates a JSON response and checks the presence of expected top-level keys (e.g., `sentiment_analysis` for the parallel agent).
- Consider adding GitHub Actions to run these smoke checks against a test environment.

## Development recommendations

- Add explicit input/output schemas to each agent's README to make it easier to integrate these agents into larger systems.
- Pin dependency versions in `requirements.txt` for reproducibility.
- Add a `LICENSE` and `CONTRIBUTING.md` if you intend to share the repo publicly.

## Contributing

1. Fork the repository.
2. Create a branch for your feature or fix.
3. Add tests (where applicable) and update relevant README(s).
4. Open a PR describing the change.

## Next steps I can help with

- Create a `.env.example` with all env keys used across agents.
- Add a smoke-test Python script that verifies one or two agents using the ADK `/run` endpoint.
- Re-create a `docs/` folder with the earlier comprehensive README split into per-topic pages.

Tell me which next step you'd like me to take and I'll implement it.

