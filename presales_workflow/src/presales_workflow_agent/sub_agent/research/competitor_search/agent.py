from google.adk import Agent

from src.presales_workflow_agent.sub_agent.research.competitor_search.prompt.competitor_search_prompt import \
    COMPETITOR_SEARCH_PROMPT
from src.shared.agent import web_search_agent_tool
from src.shared.config.model_config import GENERIC_MODEL
from src.shared.mcp.web_scrapper_mcp import get_web_scrapper_tools
from src.shared.tool.get_artifact import get_existing_artifact
from src.shared.tool.save_artifact import save_artifact


async def create_customer_competitors_search_agent() -> Agent:
    web_scrapper_tools = await get_web_scrapper_tools()

    return Agent(
        name="customer_competitors_search_agent",
        model=GENERIC_MODEL,
        description="Agent providing search capabilities for customer competitors.",
        instruction=COMPETITOR_SEARCH_PROMPT,
        tools=[
            get_existing_artifact,
            web_search_agent_tool,
            save_artifact,
            *web_scrapper_tools,
        ],
    )
