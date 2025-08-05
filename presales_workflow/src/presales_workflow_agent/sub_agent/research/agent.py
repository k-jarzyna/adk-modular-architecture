from google.adk.agents import ParallelAgent
from src.presales_workflow_agent.sub_agent.research.competitor_search.agent import customer_competitors_search_agent

from src.presales_workflow_agent.sub_agent.research.experience_analysis.agent import \
    company_experience_analysis_agent
from src.presales_workflow_agent.sub_agent.research.lead_information_retrieval.agent import \
    lead_information_retrieval_agent
from src.presales_workflow_agent.sub_agent.research.market_analysis.agent import market_analysis_agent
from src.presales_workflow_agent.sub_agent.research.of_the_shelf_solutions.agent import \
    of_the_shelf_solution_search_agent

research_manager_agent = ParallelAgent(
    name="research_manager_agent",
    description="Agent managing research stage.",
    sub_agents=[
        company_experience_analysis_agent,
        customer_competitors_search_agent,
        market_analysis_agent,
        lead_information_retrieval_agent,
        of_the_shelf_solution_search_agent
    ],
)
