# Google ADK — Example Agents (minimal)

Minimal collection of small example agents built with the Google Agent Development Kit (ADK).

This README provides only the essential information to get started.

## Quick start (Windows PowerShell)

1. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

3. Add environment variables in a `.env` file at the repo root if needed (examples are agent-specific).

4. Start ADK services you need (optional):

```powershell
# ADK web UI
adk web --port 9000

# ADK API server
adk api_server --port 9000
```

5. Run an example via the ADK API (example request to a running API server):

```powershell
# example: POST /run to execute an agent
curl -X POST "http://localhost:8000/run" -H "Content-Type: application/json" -d '{"app_name":"agent1","user_id":"u_123","session_id":"s_123","new_message":{"role":"user","parts":[{"text":"Hello from ADK"}]}}'
```



