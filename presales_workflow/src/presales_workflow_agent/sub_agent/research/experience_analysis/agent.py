from google.adk import Agent

from src.presales_workflow_agent.sub_agent.research.experience_analysis.prompt.experience_analysis_prompt import \
    EXPERIENCE_ANALYSIS_PROMPT
from src.shared.agent import knowledge_base_remote_agent_tool
from src.shared.config.model_config import GENERIC_MODEL
from src.shared.tool.get_artifact import get_existing_artifact
from src.shared.tool.save_artifact import save_artifact


company_experience_analysis_agent = Agent(
        name="company_experience_analysis_agent",
        model=GENERIC_MODEL,
        description="Agent providing search capabilities for previous company experience with specified business domain, technology or client.",
        instruction=EXPERIENCE_ANALYSIS_PROMPT,
        tools=[get_existing_artifact, save_artifact, knowledge_base_remote_agent_tool],
    )
