Agent: agent1

Purpose
- Minimal example Agent demonstrating a simple LLM-based assistant.

Key file
- `firstagent.py` — defines `root_agent` (Agent) using `gemini-2.5-flash`.

Inputs/Outputs
- Input: free-text user prompt.
- Output: assistant text response (returned by the ADK runtime).

Env / Requirements
- `GEMINI_MODEL` (optional) to override model id.
- Python deps in `requirements.txt`.

Quick run (assuming ADK server running):
```powershell
curl -X POST "http://localhost:8000/run" -H "Content-Type: application/json" -d '{"app_name":"agent1","user_id":"u_123","session_id":"s_123","new_message":{"role":"user","parts":[{"text":"Hello"}]}}'
```

Notes
- The file contains a small `__main__` example that runs `root_agent.run_async("Hello!")` for quick local testing.