from google.adk.agents import Agent
from dotenv import load_dotenv
import os
load_dotenv()


root_agent = Agent(
    name="agent1",
    model="gemini-2.5-flash", #gemini-2.5-flash-image
    description="An AI assistant that answers user questions clearly.",
    instruction="""
    You are a knowledgeable AI assistant.
    Answer user questions with accurate, up-to-date information.
    Be direct, clear, and conversational.
    """
)

if __name__ == "__main__":
    import asyncio
    asyncio.run(root_agent.run_async("Hello!"))
