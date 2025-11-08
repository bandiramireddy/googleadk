from google.adk.agents import Agent
from google.adk.tools.bigquery import BigQueryCredentialsConfig, BigQueryToolset
from google.adk.tools.bigquery.config import BigQueryToolConfig, WriteMode
from google.oauth2 import service_account
from google.genai import types
import os
from dotenv import load_dotenv 
load_dotenv()
# --- Path to your service account key file ---
SERVICE_ACCOUNT_PATH = os.path.join("../", "service-key.json")
print(SERVICE_ACCOUNT_PATH)
# --- Load credentials from the service account file ---
service_credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_PATH
)

# --- Configure the BigQuery tool ---
tool_config = BigQueryToolConfig(write_mode=WriteMode.BLOCKED)

# --- Configure the credentials for the toolset ---
credentials_config = BigQueryCredentialsConfig(
    credentials=service_credentials
)

# --- Create the BigQuery toolset ---
bigquery_toolset = BigQueryToolset(
    credentials_config=credentials_config,
    bigquery_tool_config=tool_config
)

# --- Define your agent ---
root_agent = Agent(
    name="agent3_bigquery",
    model="gemini-2.0-flash",
    description=(
        "Agent that answers questions about BigQuery data and executes SQL queries."
    ),
    instruction="""\
        Hello! I'm your friendly Data Assistant, here to help you explore your BigQuery data.
        My goal is to use the BigQuery tools I have to run queries,
        analyze the results quickly, and explain the data insights in a clear, easy-to-understand way.
        Ask me anything about your datasets!
    """,
    tools=[bigquery_toolset]
)
