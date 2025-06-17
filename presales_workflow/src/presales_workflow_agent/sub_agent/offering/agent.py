from google.adk.agents import ParallelAgent

from src.presales_workflow_agent.sub_agent.offering.internal_presales_summary_agent.agent import \
    create_internal_presales_summary_agent
from src.presales_workflow_agent.sub_agent.offering.mvp_offer_agent.agent import \
    create_mvp_offer_agent
from src.presales_workflow_agent.sub_agent.offering.product_offer_agent.agent import \
    create_product_offer_agent
from src.presales_workflow_agent.sub_agent.offering.services_offer_agent.agent import \
    create_services_offer_agent
from src.presales_workflow_agent.sub_agent.offering.workshop_offer_agent.agent import \
    create_workshop_offer_agent


async def create_offering_manager_agent() -> ParallelAgent:
    mvp_offer_agent = await create_mvp_offer_agent()
    workshop_offer_agent = await create_workshop_offer_agent()
    services_offer_agent = await create_services_offer_agent()
    product_offer_agent = await create_product_offer_agent()
    internal_presales_summary_agent = await create_internal_presales_summary_agent()

    return ParallelAgent(
        name="offering_manager_agent",
        description="Agent managing offering stage workflow",
        sub_agents=[
            mvp_offer_agent,
            workshop_offer_agent,
            services_offer_agent,
            product_offer_agent,
            internal_presales_summary_agent,
        ],
    )
