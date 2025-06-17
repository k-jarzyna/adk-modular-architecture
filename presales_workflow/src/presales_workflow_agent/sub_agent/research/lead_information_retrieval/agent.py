from google.adk import Agent

from src.presales_workflow_agent.sub_agent.research.lead_information_retrieval.prompt.lead_information_retrieval_prompt import \
    LEAD_INFORMATION_RETRIEVAL_PROMPT
from src.shared.agent import web_search_agent_tool
from src.shared.config.model_config import GENERIC_MODEL
from src.shared.mcp.web_scrapper_mcp import get_web_scrapper_tools
from src.shared.tool.get_artifact import get_existing_artifact
from src.shared.tool.save_artifact import save_artifact


async def create_lead_information_retrieval_agent() -> Agent:
    web_scrapper_tools = await get_web_scrapper_tools()

    return Agent(
        model=GENERIC_MODEL,
        name="lead_information_retrieval_agent",
        description="Agent providing customer information retrieval capabilities.",
        instruction=LEAD_INFORMATION_RETRIEVAL_PROMPT,
        tools=[
            web_search_agent_tool,
            get_existing_artifact,
            *web_scrapper_tools,
            save_artifact,
        ],
    )
