from google.adk.agents import LlmAgent 
from google.adk.tools.google_search_tool import google_search
from dotenv import load_dotenv
import os,requests
load_dotenv()

 

root_agent = LlmAgent(
    name="agent_builtintools", 
    model="gemini-2.5-flash",
    description="A helpful assistant that can check the weather and perform simple arithmetic.",
    instruction="""
    You are a kind and helpful AI assistant.
    """,
    tools=[google_search]  
)