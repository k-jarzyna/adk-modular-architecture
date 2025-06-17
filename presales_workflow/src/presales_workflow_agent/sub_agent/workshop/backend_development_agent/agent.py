from google.adk import Agent

from src.presales_workflow_agent.sub_agent.workshop.schema.workshop_result_schema import \
    WORKSHOP_RESULT_TEMPLATE
from src.shared.agent import knowledge_base_remote_agent_tool
from src.shared.artifact.artifact_definition import (
    BACKEND_DEVELOPMENT_WORKSHOP_ARTIFACT, COMPANY_EXPERIENCE_ARTIFACT,
    COMPETITORS_ARTIFACT, CUSTOMER_INFORMATION_ARTIFACT,
    MARKET_ANALYSIS_ARTIFACT, OF_THE_SHELF_SOLUTIONS_ARTIFACT,
    PROJECT_DESCRIPTION_ARTIFACT)
from src.shared.config.model_config import GENERIC_MODEL
from src.shared.tool.get_artifact import get_existing_artifact
from src.shared.tool.save_artifact import save_artifact

from src.presales_workflow_agent.sub_agent.workshop.backend_development_agent.prompt.backend_development_prompt import \
    BACKEND_DEVELOPMENT_PROMPT

backend_development_agent = Agent(
    model=GENERIC_MODEL,
    name="backend_development_agent",
    description="Agent performing presales analysis from a backend developer perspective",
    instruction=BACKEND_DEVELOPMENT_PROMPT,
    tools=[get_existing_artifact, save_artifact, knowledge_base_remote_agent_tool],
)
