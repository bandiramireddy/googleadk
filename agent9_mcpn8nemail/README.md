Agent: agent9_mcpn8nemail

Purpose
- Demonstrates using an MCP toolset to compose and send emails programmatically.

Key file
- `agent9_mcpn8nemail.py` — configures `emailsend_mcp_toolset` (MCPToolset) and an `LlmAgent` that uses it.

Inputs/Outputs
- Input: user requests to compose/send email.
- Output: email draft and send confirmation; agent will confirm recipient/subject/body before sending.

Env / Requirements
- MCP endpoint URL for the email service (configured in the file).

Quick run
- Ensure the MCP email endpoint is reachable and authorized. Use ADK `/run` with a request to compose an email.

Notes
- The agent enforces confirmation before sending to avoid unintended emails.