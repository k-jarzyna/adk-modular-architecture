from google.adk.agents import ParallelAgent

from src.presales_workflow_agent.sub_agent.research.competitor_search.agent import \
    create_customer_competitors_search_agent
from src.presales_workflow_agent.sub_agent.research.experience_analysis.agent import \
    create_company_experience_analysis_agent
from src.presales_workflow_agent.sub_agent.research.lead_information_retrieval.agent import \
    create_lead_information_retrieval_agent
from src.presales_workflow_agent.sub_agent.research.market_analysis.agent import \
    create_market_analysis_agent
from src.presales_workflow_agent.sub_agent.research.of_the_shelf_solutions.agent import \
    create_of_the_shelf_solution_search_agent


async def create_research_manager_agent() -> ParallelAgent:
    customer_competitors_search_agent = await create_customer_competitors_search_agent()
    of_the_shelf_solution_search_agent = (
        await create_of_the_shelf_solution_search_agent()
    )
    lead_information_retrieval_agent = await create_lead_information_retrieval_agent()
    company_experience_analysis_agent = await create_company_experience_analysis_agent()
    market_analysis_agent = await create_market_analysis_agent()

    return ParallelAgent(
        name="research_manager_agent",
        description="Agent managing research stage.",
        sub_agents=[
            company_experience_analysis_agent,
            customer_competitors_search_agent,
            market_analysis_agent,
            lead_information_retrieval_agent,
            of_the_shelf_solution_search_agent,
        ],
    )
