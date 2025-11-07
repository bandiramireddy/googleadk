import os
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPConnectionParams
from dotenv import load_dotenv

load_dotenv()
TAVILY_API_KEY=os.getenv("TAVILY_API_KEY")
# ------------------------------
#  MCPToolset connection to FastMCP server
# ------------------------------
# tavily_mcp_toolset = MCPToolset(
#     connection_params=StreamableHTTPConnectionParams(
#         url="https://mcp.tavily.com/mcp/?tavilyApiKey=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"  # Your FastMCP server URL
#     )
# )

tavily_mcp_toolset = MCPToolset(
    connection_params=StreamableHTTPConnectionParams(
        url="https://mcp.tavily.com/mcp/",
        headers={
            "Authorization": "Bearer "+TAVILY_API_KEY  # your API token
        }
    )
)
# ------------------------------
#  Create ADK LlmAgent using MCP toolset
# ------------------------------
root_agent = LlmAgent(
    model="gemini-2.0-flash",
    name="agent6_mcptavilysearch",
    instruction = """
            You are a **helpfull Assistant** that provides up-to-date, factual answers.
            You have access to the `tavily_mcp_toolset`
              (a real-time web search and content extraction tool).
            """,
    tools=[tavily_mcp_toolset]  # MCPToolset instance
)


