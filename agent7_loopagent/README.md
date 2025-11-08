Agent: FullArticleWorkflow (Loop)

Purpose
- Iterative article generation and refinement using a `LoopAgent` with writer, editor, and critic.

Key file
- `agent_loopagent.py` — defines `ArticleWriter`, `ArticleEditor`, `ArticleCritic`, wrapped in a `LoopAgent` (`ContentRefinementLoop`) and a `SequentialAgent` root (`FullArticleWorkflow`).

Inputs/Outputs
- Input: topic or prompt to write about.
- Output state keys: `article_draft`, `critique_feedback`.

Env / Requirements
- `GEMINI_MODEL` (configured in code) and `requests` if external tools are used.

Quick run
- Use ADK `/run` with a prompt to generate an article. The workflow will iterate up to `max_iterations` or until the critic triggers `exit_loop()`.

Notes
- The critic may call a tool (commented example `exit_loop`) to signal loop termination — adapt as needed.