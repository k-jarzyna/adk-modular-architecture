from google.adk import Agent

from src.presales_workflow_agent.sub_agent.offering.workshop_offer_agent.prompt.workshop_offer_prompt import \
    WORKSHOP_OFFER_PROMPT
from src.shared.agent import knowledge_base_remote_agent_tool
from src.shared.config.model_config import GENERIC_MODEL
from src.shared.tool.get_artifact import get_existing_artifact
from src.shared.tool.save_artifact import save_artifact


workshop_offer_agent = Agent(
    model=GENERIC_MODEL,
    name="workshop_offer_agent",
    description="Agent generating a workshop offer to better understand client's product needs",
    instruction=WORKSHOP_OFFER_PROMPT,
    tools=[save_artifact, get_existing_artifact, knowledge_base_remote_agent_tool],
)
