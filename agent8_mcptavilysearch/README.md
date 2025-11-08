Agent: agent6_mcptavilysearch

Purpose
- Shows integration with a remote MCP toolset (Tavily/ FastMCP) to provide real-time web search/extraction capabilities.

Key file
- `agent_tavilysearch.py` — creates `tavily_mcp_toolset` using `MCPToolset` and an API key, then an `LlmAgent` using that toolset.

Inputs/Outputs
- Input: user questions requiring web search or fresh content.
- Output: LLM answer augmented by MCP tool results.

Env / Requirements
- `TAVILY_API_KEY` (set in `.env` or env).
- MCP service reachable at the configured URL.

Quick run
- Ensure MCP endpoint is reachable and `TAVILY_API_KEY` is set. Run ADK and `/run` with a query that requires real-time search.

Notes
- Secure your API key and restrict access to the MCP endpoint.