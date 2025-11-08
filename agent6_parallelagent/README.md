Agent: Investment_Analyst_Agent (Parallel)

Purpose
- Demonstrates `ParallelAgent` composed of three analysis LlmAgents: Sentiment, Valuation, and Risk.

Key file
- `agent_parallelagent.py` — defines `sentiment_agent`, `valuation_agent`, `risk_agent` and the `ParallelAgent` parent.
- Diagram: `ParallelInvestmentAnalyst.drawio` (visualizes the parallel composition).

Inputs/Outputs
- Input: stock ticker or user prompt asking for analysis.
- Output/state keys: `sentiment_analysis`, `valuation_summary`, `risk_assessment`.

Env / Requirements
- `GEMINI_MODEL` (defaults to `gemini-2.5-flash` in the file).

Quick run
- Start ADK and call `/run` with message asking for stock analysis. The three sub-agents run concurrently and their outputs are aggregated.

Notes
- Good pattern for independent analysis steps that can run in parallel to reduce wall-clock time.