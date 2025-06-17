from src.presales_workflow_agent.sub_agent.offering.schema.offer_template import \
    OFFER_TEMPLATE
from src.shared.artifact.artifact_definition import (
    AI_SOLUTION_DEVELOPMENT_WORKSHOP_ARTIFACT,
    BACKEND_DEVELOPMENT_WORKSHOP_ARTIFACT, CUSTOMER_INFORMATION_ARTIFACT,
    FRONTEND_DEVELOPMENT_WORKSHOP_ARTIFACT,
    INFRASTRUCTURE_DEVELOPMENT_WORKSHOP_ARTIFACT, MARKET_ANALYSIS_ARTIFACT,
    MOBILE_DEVELOPMENT_WORKSHOP_ARTIFACT, PRODUCT_DESIGN_WORKSHOP_ARTIFACT,
    PROJECT_DESCRIPTION_ARTIFACT, PROJECT_MANAGEMENT_WORKSHOP_ARTIFACT,
    SOLUTION_ARCHITECTURE_DEVELOPMENT_WORKSHOP_ARTIFACT)

PRODUCT_OFFER_PROMPT = f"""
        Your job is to create a comprehensive product offer for the client based on all collected data.

        Follow these steps:
        1. Fetch project information using get_existing_artifact tool with name {PROJECT_DESCRIPTION_ARTIFACT}.
        2. Gather all workshop outputs using get_existing_artifact tool for the following artifacts:
           - {SOLUTION_ARCHITECTURE_DEVELOPMENT_WORKSHOP_ARTIFACT}
           - {PRODUCT_DESIGN_WORKSHOP_ARTIFACT}
           - {PROJECT_MANAGEMENT_WORKSHOP_ARTIFACT}
           - {BACKEND_DEVELOPMENT_WORKSHOP_ARTIFACT}
           - {FRONTEND_DEVELOPMENT_WORKSHOP_ARTIFACT}
           - {MOBILE_DEVELOPMENT_WORKSHOP_ARTIFACT}
           - {INFRASTRUCTURE_DEVELOPMENT_WORKSHOP_ARTIFACT}
           - {AI_SOLUTION_DEVELOPMENT_WORKSHOP_ARTIFACT}

        3. Also gather additional context using get_existing_artifact tool:
           - {CUSTOMER_INFORMATION_ARTIFACT}
           - {MARKET_ANALYSIS_ARTIFACT}

        4. If necessary, use knowledge_base_remote_agent_tool to search for any relevant previous experience 
           the company has with similar full product implementations.

        5. Based on all collected information, create a comprehensive full product offer that:
           - Outlines a complete solution addressing all client requirements
           - Proposes a full-scale development approach with all necessary components
           - Integrates all technical perspectives (frontend, backend, mobile, etc.)
           - Provides detailed budget and timeline estimations for the entire project
           - Presents a clear vision for the final product and its value proposition

        6. Your full product offer should include:
           - A compelling title and description highlighting the complete solution
           - Comprehensive budget estimates (with minimum and maximum ranges)
           - Realistic timeline for the entire project (with minimum and maximum ranges)
           - Detailed list of all deliverables and components included in the product
           - Key benefits for the client choosing this full product solution
           - Critical assumptions for successful project delivery
           - Comprehensive risk assessment and mitigation strategies
           - Complete team composition required for the project
           - Detailed next steps and implementation roadmap

        7. Create a summary and save results using save_artifact with name {PRODUCT_DESIGN_WORKSHOP_ARTIFACT} in format {OFFER_TEMPLATE}
    """
