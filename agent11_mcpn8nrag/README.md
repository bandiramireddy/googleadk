Agent: agent9_mcpn8nrag

Purpose
- Example of a RAG-style agent connected via MCP to a vector store (e.g., Pinecone) for retrieval-augmented responses.

Key file
- `agent_mcpn8nrag.py` — configures `mcp_n8n_rag` MCPToolset and an `LlmAgent` that must query the vector store.

Inputs/Outputs
- Input: user questions that may require knowledge retrieval.
- Output: answers using retrieved documents. If no match found, agent returns exactly: "I don’t find any information in the vector database." per the instruction.

Env / Requirements
- MCP endpoint URL that proxies to your vector DB/RAG pipeline.

Quick run
- Ensure MCP/RAG pipeline is active and reachable. Use ADK `/run` to ask a question that relies on the vector store.

Notes
- This pattern reduces hallucination by forcing reliance on retrieved docs; ensure vector index is up to date.