from google.adk import Agent

from src.presales_workflow_agent.sub_agent.offering.services_offer_agent.prompt.services_offer_prompt import \
    SERVICES_OFFER_PROMPT
from src.shared.agent import knowledge_base_remote_agent_tool
from src.shared.config.model_config import GENERIC_MODEL
from src.shared.tool.get_artifact import get_existing_artifact
from src.shared.tool.save_artifact import save_artifact


async def create_services_offer_agent() -> Agent:
    return Agent(
        model=GENERIC_MODEL,
        name="services_offer_agent",
        description="Agent generating an offer for individual services based on company's previous experience",
        instruction=SERVICES_OFFER_PROMPT,
        tools=[save_artifact, get_existing_artifact, knowledge_base_remote_agent_tool],
    )
