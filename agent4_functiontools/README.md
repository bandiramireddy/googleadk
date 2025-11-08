Agent: agent_functiontools

Purpose
- Shows how to provide local Python functions as tools to an agent (weather and arithmetic examples).

Key file
- `agent_functiontools.py` — defines `weather_tool(location)` and `addition_tool(a,b)` and an `Agent` using them.

Inputs/Outputs
- Weather queries: agent will call `weather_tool` and return the wttr.in response.
- Addition queries: agent will call `addition_tool` and return a formatted sum string.

Env / Requirements
- `requests` package (in `requirements.txt`).
- Network access to `https://wttr.in` for weather.

Quick run
- Start ADK and send a `/run` payload asking for weather or an addition operation; the agent instruction requires using the tools when appropriate.

Notes
- This pattern is useful for deterministic functions and safe external calls.