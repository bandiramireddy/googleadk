Agent: agent8_mcpselfserver

Purpose
- Example showing an LlmAgent that calls a local FastMCP server for weather data (MCPToolset integration).

Key file
- `agent8_mcpselfserver.py` — defines `weather_mcp_toolset` pointing to `http://127.0.0.1:8100/mcp` and an `LlmAgent` using it.

Inputs/Outputs
- Input: weather-related user prompts.
- Output: responses using MCP tool results when available.

Env / Requirements
- Local MCP server running at the configured URL.

Quick run
- Start the local MCP server, then start ADK and call the agent via `/run` to query weather.

Notes
- Update the MCP URL in the file if your MCP service is hosted elsewhere.