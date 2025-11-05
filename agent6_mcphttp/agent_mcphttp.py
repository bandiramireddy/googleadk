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
        url="http://127.0.0.1:8000/mcp"  # Your FastMCP server URL
    )
)

emailsend_mcp_toolset = MCPToolset(
    connection_params=StreamableHTTPConnectionParams(
        url="http://localhost:5678/mcp/cf00a9b9-2b2f-4917-8daf-e86f6f245cc7" #make this should be PRD url
    )
)
# 
# ------------------------------
#  Create ADK LlmAgent using MCP toolset
# ------------------------------
root_agent = LlmAgent(
    model="gemini-2.0-flash",
    name="agent_mcphttp",
    instruction = """
            You are an intelligent assistant capable of retrieving weather information 
             and sending emails for any purpose.

             You have access to two external MCP toolsets:
             1. `weather_mcp_toolset` — to get current or forecast weather data.
             2. `emailsend_mcp_toolset` — to compose and send emails on behalf of the user.

             Behavior:
             - Use `weather_mcp_toolset` when the user explicitly requests weather info.
             - Use `emailsend_mcp_toolset` whenever the user asks you to send an email, for any topic.
             - Always confirm recipient email, subject, and message body before sending.
             - format subject and body appropriately based on user context, you can ask user for more details if needed.
             - use your inteligence to format the email in a professional manner.
             - Be polite, clear, and professional in all responses.
             """,
    tools=[weather_mcp_toolset,emailsend_mcp_toolset]  # MCPToolset instance
)


