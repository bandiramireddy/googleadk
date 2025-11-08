from google.adk.agents import LlmAgent, LoopAgent,SequentialAgent
from google.adk.tools import ToolContext
from dotenv import load_dotenv
import os
load_dotenv()

# def exit_loop(tool_context: ToolContext):
#     """Call this function ONLY when the critique indicates no further changes are needed, 
#     signaling the iterative process should end."""
#     print(f"  [Tool Call] exit_loop triggered by {tool_context.agent_name}")
#     # Setting this flag is the mechanism to break out of a LoopAgent
#     tool_context.actions.escalate = True 
#     # Tools should typically return JSON-serializable output
#     return {"status": "Loop terminated successfully"}

# Agent 1 (Generator - No change)
article_writer = LlmAgent(
    name="ArticleWriter",
    model="gemini-2.5-flash",
    instruction="""You are a creative article writer. Write engaging first drafts on the topic. 
    Focus on ideas and content flow. Keep articles between 250-350 words.
    Store the final article text in the 'article_draft' state key.""",
    output_key="article_draft" 
)

# Agent 2 (Refiner - Now uses feedback)
article_editor = LlmAgent(
    name="ArticleEditor",
    model="gemini-2.5-flash",
    instruction="""You are a professional editor. Refine the article: {article_draft}.
    **Prioritize addressing the critique: {critique_feedback?}** (if not present take as empty dont throw error ).  
    Improve clarity, grammar, and engagement. Return ONLY the refined article.""",
    output_key="article_draft"
)

# Agent 3 (Critic/Checker - Provides feedback or terminates)
article_critic = LlmAgent(
    name="ArticleCritic",
    model="gemini-2.5-flash", 
    instruction="""Critique the current article draft: {article_draft}.
    Check for two things: 1. Is the flow logical? 2. Is the tone professional?
    
    # If the article is **PERFECT** and ready to publish, **call the exit_loop() tool** immediately. 
    # DO NOT output any text or critique if you call the tool.
    
    If you find an issue, provide **specific, actionable feedback** for the editor (e.g., 'The introduction is too vague.') and DO NOT call the tool.""",
    # The output key captures the feedback if the tool is NOT called
    output_key="critique_feedback" 
) 

refinement_loop = LoopAgent(
    name="ContentRefinementLoop",
    sub_agents=[
        article_editor,   # Refine
        article_critic    # Critique and set state for next check
    ],
    max_iterations=2,
    description="A loop agent that refines an article draft based on iterative critique."
)

# --- Root Agent (Sequence) ---
# Use a SequenceAgent to run the Writer once, then start the Loop.

root_agent = SequentialAgent(
    name="FullArticleWorkflow",
    sub_agents=[
        article_writer,       # Step 1: Generate initial draft
        refinement_loop       # Step 2: Iterate until 'PERFECT' or max_iterations
    ],
    description="Generates an article and iteratively refines it based on critical feedback."
)
