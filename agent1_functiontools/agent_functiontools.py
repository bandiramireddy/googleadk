from google.adk.agents import Agent 
from dotenv import load_dotenv
import os,requests
load_dotenv()

# --- Tool Definitions (Recommended structure to avoid parsing issues) ---

def weather_tool(location: str) -> str:
    """Get the real-time weather for a location (uses free wttr.in API)."""
    try:
        # wttr.in provides simple weather text for any city
        url = f"https://wttr.in/{location}?format=3"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.text  # Example: "London: 🌦 +18°C"
    except Exception as e:
        return f"Unable to fetch weather for {location}: {e}"

def addition_tool(a: int, b: int) -> str:
    """Calculates the sum of two integers."""
    # Using type hints like 'int' for numbers is best practice.
    return f"The sum of {a} and {b} is {a + b}."
 

root_agent = Agent(
    name="agent_functiontools", 
    model="gemini-2.5-flash",
    description="A helpful assistant that can check the weather and perform simple arithmetic.",
    instruction="""
    You are a kind and helpful AI assistant.
    
    You MUST analyze the user's request to determine if it requires using one of your available tools: `weather_tool` or `addition_tool`.

    1.  **For weather-related questions**, you MUST use the `weather_tool` with the location provided by the user.
    2.  **For mathematical questions involving addition**, you MUST use the `addition_tool`.
    3.  for any other type of question, you MAY use the `google_Search` tool to find relevant information.
    """,
    tools=[weather_tool,addition_tool]  
)