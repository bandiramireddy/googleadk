import os
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPConnectionParams
from dotenv import load_dotenv

load_dotenv()

# ------------------------------
#  MCPToolset connection to FastMCP server
# ------------------------------
weather_mcp_toolset = MCPToolset(
    connection_params=StreamableHTTPConnectionParams(
        url="http://127.0.0.1:8100/mcp"  # Your FastMCP server URL
    )
)

# 
# ------------------------------
#  Create ADK LlmAgent using MCP toolset
# ------------------------------
root_agent = LlmAgent(
    model="gemini-2.0-flash",
    name="agent8_mcpselfserver",
    instruction = """
           You are a helpful AI assistant.

            Use the `weather_mcp_toolset` when the user asks for weather information.
            If the tool fails, inform the user.

            Be clear, factual, and polite.
            Avoid guessing or making up information.
             """,
    tools=[weather_mcp_toolset]  # MCPToolset instance
)


