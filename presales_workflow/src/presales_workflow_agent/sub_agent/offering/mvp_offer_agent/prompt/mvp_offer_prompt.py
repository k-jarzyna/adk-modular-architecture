from src.presales_workflow_agent.sub_agent.offering.schema.offer_template import \
    OFFER_TEMPLATE
from src.shared.artifact.artifact_definition import (
    CUSTOMER_INFORMATION_ARTIFACT, MARKET_ANALYSIS_ARTIFACT,
    MVP_OFFER_ARTIFACT, PRODUCT_DESIGN_WORKSHOP_ARTIFACT,
    PROJECT_DESCRIPTION_ARTIFACT, PROJECT_MANAGEMENT_WORKSHOP_ARTIFACT,
    SOLUTION_ARCHITECTURE_DEVELOPMENT_WORKSHOP_ARTIFACT)

MVP_OFFER_PROMPT = f"""
        Your job is to create a well-crafted MVP (Minimum Viable Product) offer for the client based on all collected data.
        
        Follow these steps:
        1. Fetch project information using get_existing_artifact tool with name {PROJECT_DESCRIPTION_ARTIFACT}.
        2. Gather all key workshop outputs using get_existing_artifact tool for the following artifacts:
           - {SOLUTION_ARCHITECTURE_DEVELOPMENT_WORKSHOP_ARTIFACT}
           - {PRODUCT_DESIGN_WORKSHOP_ARTIFACT}
           - {PROJECT_MANAGEMENT_WORKSHOP_ARTIFACT}
           
        3. Also gather additional context using get_existing_artifact tool:
           - {CUSTOMER_INFORMATION_ARTIFACT}
           - {MARKET_ANALYSIS_ARTIFACT}
        
        4. If necessary, use knowledge_base_remote_agent_tool to search for any relevant previous experience 
           the company has with similar MVP projects and proposals.
        
        5. Based on all collected information, create a comprehensive MVP offer that:
           - Focuses on delivering core functionality in a minimized scope
           - Proposes a more economical and faster approach than a full product
           - Identifies the essential features that would provide immediate value
           - Provides realistic budget and timeline estimations for the MVP
           - Outlines a clear path to validate the product idea with minimal investment
        
        6. Your MVP offer should include:
           - A compelling title and description focused on the MVP approach
           - Clear budget estimates (with minimum and maximum ranges)
           - Realistic timeline (with minimum and maximum ranges in weeks)
           - List of specific services and deliverables included in the MVP
           - Key benefits for the client choosing the MVP approach
           - Important assumptions about the MVP development
           - Potential risks and mitigations for the MVP approach
           - Proposed team composition for the MVP project
           - Clear next steps if the client decides to proceed with the MVP
           
        7. Create a summary and save results using save_artifact tool with name {MVP_OFFER_ARTIFACT} in format {OFFER_TEMPLATE}
    """