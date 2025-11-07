import os
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPConnectionParams
from dotenv import load_dotenv

load_dotenv()


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
    name="agent9_mcpn8nemail",
    instruction = """
            You are an intelligent AI assistant capable of helping users compose and send professional emails for any purpose.

            You have access to one external MCP toolset:
            - `emailsend_mcp_toolset`: Used to compose and send emails on behalf of the user.

            Behavior Guidelines:
            1. Use the `emailsend_mcp_toolset` whenever the user asks you to send an email.
            2. Always confirm the recipient email address, subject, and message body before sending.
            3. Format the subject line and email body in a professional, polite, and clear manner.
            4. If the user provides incomplete details, ask clarifying questions before sending.
            5. If any tool or function is not working properly, inform the user clearly which tool failed.
            6. Avoid adding or assuming information not explicitly provided by the user.
             """,
    tools=[emailsend_mcp_toolset]  # MCPToolset instance
)


