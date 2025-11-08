import os
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPConnectionParams
from dotenv import load_dotenv

load_dotenv()



mcp_n8n_rag = MCPToolset(
    connection_params=StreamableHTTPConnectionParams(
        url="http://localhost:5678/mcp/58b264ee-a1f3-459c-aa81-89eb8fc0a032" #make this should be PRD url
    )
)
# 
# ------------------------------
#  Create ADK LlmAgent using MCP toolset
# ------------------------------
root_agent = LlmAgent(
    model="gemini-2.0-flash",
    name="agent9_mcpn8nrag",
    instruction = """
            You are a helpful AI assistant.

            You are connected to a Pinecone vector store, which you can use to retrieve relevant information to answer user queries.

            When a user asks a question:
            1. First, search the Pinecone vector store for relevant data.
            2. If relevant information is found, use it to generate a clear, concise, and accurate response.
            3. If no relevant information is found, respond exactly with:
            "I don’t find any information in the vector database."

            Guidelines:
            - Do not invent or assume any information not found in the vector store.
            - Keep answers factual and to the point.
            - Maintain a polite and professional tone at all times.
             """,
    tools=[mcp_n8n_rag]  # MCPToolset instance
)


