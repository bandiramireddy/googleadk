Agent: BigQuery_Agent

Purpose
- Demonstrates using ADK's BigQuery toolset to run queries and analyze BigQuery datasets.

Key file
- `agent_bigquery.py` — configures `BigQueryToolset` with service account credentials and constructs an `Agent` that uses it.

Inputs/Outputs
- Input: natural language questions about data; agent translates to SQL using tools.
- Output: query results and analysis provided by the LLM.

Env / Requirements
- A Google service account JSON key file; set `SERVICE_ACCOUNT_PATH` or adjust code to point to your key.
- `google-auth` and BigQuery client libraries in `requirements.txt`.

Quick run
- Ensure service account permissions for BigQuery and update `SERVICE_ACCOUNT_PATH`. Start ADK and call the agent with a data question.

Notes
- Never commit service account keys to the repo. Use IAM best practices.