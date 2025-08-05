from dotenv import load_dotenv
load_dotenv()

from google.adk.tools import AgentTool
from src.shared.config.model_config import GENERIC_MODEL
from src.presales_workflow_agent.sub_agent.document_analysis.agent import document_analysis_manager_agent
from src.presales_workflow_agent.sub_agent.offering.agent import offering_manager_agent
from src.presales_workflow_agent.sub_agent.research.agent import research_manager_agent
from src.presales_workflow_agent.sub_agent.workshop.agent import workshop_manager_agent
from src.shared.agent.knowledge_base_remote_agent import knowledge_agent
from src.shared.tool.get_artifact import get_existing_artifact
from src.shared.tool.list_artifacts import list_artifacts
from src.shared.tool.save_artifact import save_artifact
from google.adk.agents import LlmAgent, SequentialAgent
from src.presales_workflow_agent.prompt.root_agent_prompt import ROOT_AGENT_PROMPT


presales_sequence_agent = SequentialAgent(
    sub_agents=[
        document_analysis_manager_agent,
        research_manager_agent,
        workshop_manager_agent,
        offering_manager_agent
    ],
    name="presales_sequence_agent",
    description="Presales Process Sequence Agent",
)

root_agent = LlmAgent(
    model=GENERIC_MODEL,
    description="Presales Workflow Agent",
    name="presales_workflow_agent",
    sub_agents=[
        presales_sequence_agent
    ],
    instruction=ROOT_AGENT_PROMPT,
    tools=[
        save_artifact,
        get_existing_artifact,
        list_artifacts,
        AgentTool(knowledge_agent)
    ],
)