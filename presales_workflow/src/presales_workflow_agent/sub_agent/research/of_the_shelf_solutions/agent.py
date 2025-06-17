from google.adk import Agent

from src.presales_workflow_agent.sub_agent.research.of_the_shelf_solutions.prompt.of_the_shelf_solutions_prompt import \
    OF_THE_SHELF_SOLUTIONS_PROMPT
from src.shared.agent import web_search_agent_tool
from src.shared.config.model_config import GENERIC_MODEL
from src.shared.mcp.web_scrapper_mcp import get_web_scrapper_tools
from src.shared.tool.get_artifact import get_existing_artifact
from src.shared.tool.save_artifact import save_artifact


async def create_of_the_shelf_solution_search_agent() -> Agent:
    web_scrapper_tools = await get_web_scrapper_tools()

    return Agent(
        name="of_the_shelf_solution_search_agent",
        model=GENERIC_MODEL,
        description="Agent providing search capabilities for existing of the shelf alternative solutions.",
        instruction=OF_THE_SHELF_SOLUTIONS_PROMPT,
        tools=[
            get_existing_artifact,
            web_search_agent_tool,
            *web_scrapper_tools,
            save_artifact,
        ],
    )
