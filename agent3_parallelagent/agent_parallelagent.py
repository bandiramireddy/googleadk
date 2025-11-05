from google.adk.agents  import ParallelAgent, LlmAgent 
from dotenv import load_dotenv
import os
load_dotenv()
GEMINI_MODEL = "gemini-2.5-flash"
from dotenv import load_dotenv
import os
load_dotenv()
GEMINI_MODEL = "gemini-2.5-flash"

# --- 1. Sentiment Analysis Agent ---
sentiment_agent = LlmAgent(
    name="SentimentAgent",
    model=GEMINI_MODEL,
    instruction="""
    You are a market sentiment analyst. Analyze recent news and social media buzz 
    for the stock ticker provided by the user. Classify the overall sentiment as 
    'Bullish', 'Neutral', or 'Bearish', and provide 3 key supporting facts.
    """,
    output_key="sentiment_analysis"
)

# --- 2. Quick Valuation Agent ---
valuation_agent = LlmAgent(
    name="ValuationAgent",
    model=GEMINI_MODEL,
    instruction="""
    You are a financial health expert. Provide a concise valuation summary for the 
    stock ticker. Focus on key metrics: P/E ratio, recent revenue growth rate, and 
    debt-to-equity ratio. State whether the stock appears 'Overvalued', 'Fairly Valued', 
    or 'Undervalued' based on a simple comparison to its sector.
    """,
    output_key="valuation_summary"
)

# --- 3. Risk Assessment Agent ---
risk_agent = LlmAgent(
    name="RiskAgent",
    model=GEMINI_MODEL,
    instruction="""
    You are an investment risk specialist. Identify the top 3 specific risks associated 
    with the stock ticker (e.g., regulatory changes, new competitors, high volatility). 
    Provide a brief mitigation strategy for each risk.
    """,
    output_key="risk_assessment"
)
# The Parallel Investment Analyst Agent
investment_analyst_agent = ParallelAgent(
    name="Investment_Analyst_Agent",
    sub_agents=[sentiment_agent, valuation_agent, risk_agent],
    description="Performs concurrent sentiment, valuation, and risk analysis on a single stock ticker.",
)

root_agent = investment_analyst_agent
