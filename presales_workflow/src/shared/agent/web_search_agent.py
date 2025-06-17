from google.adk import Agent
from google.adk.tools import google_search

from src.shared.config.model_config import GENERIC_MODEL

web_search_agent = Agent(
    name="web_search_agent",
    model=GENERIC_MODEL,
    description="Agent providing web search utilities.",
    instruction="""
        You're web search agent providing web search utilities.
        Start your work by searching for information using google_search_tool.
        Respond with exact google search response.
        Do not mock response, always use search tool.""",
    tools=[google_search],
)
