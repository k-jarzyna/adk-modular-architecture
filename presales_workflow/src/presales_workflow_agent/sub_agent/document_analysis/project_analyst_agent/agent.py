from google.adk import Agent

from src.presales_workflow_agent.sub_agent.document_analysis.project_analyst_agent.prompt.prompt import \
    PROJECT_ANALYST_PROMPT
from src.shared.config.model_config import GENERIC_MODEL
from src.shared.tool.get_artifact import get_existing_artifact
from src.shared.tool.save_artifact import save_artifact

project_analyst_agent = Agent(
    model=GENERIC_MODEL,
    name="project_analyst_agent",
    description="Project analyst agent that summarizes project information based on presales document.",
    instruction=PROJECT_ANALYST_PROMPT,
    tools=[get_existing_artifact, save_artifact],
)
