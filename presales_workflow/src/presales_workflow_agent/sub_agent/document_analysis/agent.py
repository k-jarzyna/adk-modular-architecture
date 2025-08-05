from google.adk.agents import ParallelAgent

from src.presales_workflow_agent.sub_agent.document_analysis.project_analyst_agent.agent import project_analyst_agent


document_analysis_manager_agent = ParallelAgent(
    name="document_analysis_manager_agent",
    description="Agent managing document analysis stage.",
    sub_agents=[project_analyst_agent],
)
