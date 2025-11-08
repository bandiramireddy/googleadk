Agent: agent_builtintools

Purpose
- Demonstrates integrating ADK built-in tools (e.g., `google_search`) with an LLM agent.

Key file
- `agent1_builtintools.py` — defines `root_agent` (LlmAgent) with `tools=[google_search]`.

Inputs/Outputs
- Input: queries or user prompts that may require web search.
- Output: answer produced by the LLM, optionally augmented with tool results.

Env / Requirements
- Internet access to call built-in tool endpoints if required.
- `requirements.txt` installed.

Quick run
- Start ADK server and call `/run` with `app_name` pointing to this app (name discovered by ADK).

Notes
- Inspect the import `google.adk.tools.google_search_tool` to see available tool parameters.