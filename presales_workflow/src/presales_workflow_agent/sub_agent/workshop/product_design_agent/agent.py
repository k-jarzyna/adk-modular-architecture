from google.adk import Agent
from google.adk.agents import SequentialAgent

from src.presales_workflow_agent.sub_agent.workshop.schema.workshop_result_schema import \
    WORKSHOP_RESULT_TEMPLATE
from src.presales_workflow_agent.sub_agent.workshop.ui_agent import ui_agent
from src.presales_workflow_agent.sub_agent.workshop.ux_agent import ux_agent
from src.shared.agent import knowledge_base_remote_agent_tool
from src.shared.artifact.artifact_definition import (
    COMPETITORS_ARTIFACT, CUSTOMER_INFORMATION_ARTIFACT,
    MARKET_ANALYSIS_ARTIFACT, PRODUCT_DESIGN_WORKSHOP_ARTIFACT,
    PROJECT_DESCRIPTION_ARTIFACT, UI_WORKSHOP_ARTIFACT, UX_WORKSHOP_ARTIFACT)
from src.shared.config.model_config import GENERIC_MODEL
from src.shared.tool.get_artifact import get_existing_artifact
from src.shared.tool.save_artifact import save_artifact

from src.presales_workflow_agent.sub_agent.workshop.product_design_agent.prompt.product_design_prompt import \
    PRODUCT_DESIGN_PROMPT

product_design_summary_agent = Agent(
    model=GENERIC_MODEL,
    name="product_design_summary_agent",
    description="Agent creating comprehensive product design strategy based on UX and UI insights",
    instruction=PRODUCT_DESIGN_PROMPT,
    tools=[get_existing_artifact, save_artifact, knowledge_base_remote_agent_tool],
)

product_design_agent = SequentialAgent(
    name="product_design_agent",
    description="Agent managing product design workflow in sequence",
    sub_agents=[ux_agent, ui_agent, product_design_summary_agent],
)
