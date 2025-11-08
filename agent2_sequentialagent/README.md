Agent: CodePipelineAgent (Sequential)

Purpose
- Example of a sequential pipeline: code writer -> reviewer -> refactorer.

Key file
- `agent_sequentialagent.py` — defines three LlmAgents (`CodeWriterAgent`, `CodeReviewerAgent`, `CodeRefactorerAgent`) and composes them in `SequentialAgent`.

Inputs/Outputs
- Input: natural language spec for code to generate.
- Outputs/state keys: `generated_code`, `review_comments`, `refactored_code`.

Env / Requirements
- Model id via `GEMINI_MODEL` may be used.

Quick run
- Use ADK `/run` endpoint targeting the app. The sequential agent stores intermediate outputs in shared state for downstream agents.

Notes
- Output keys are useful for debugging and for passing data explicitly between steps.