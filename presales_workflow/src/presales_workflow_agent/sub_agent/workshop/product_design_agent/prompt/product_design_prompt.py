from src.shared.artifact.artifact_definition import PRODUCT_DESIGN_WORKSHOP_ARTIFACT, PROJECT_DESCRIPTION_ARTIFACT, \
    UX_WORKSHOP_ARTIFACT, UI_WORKSHOP_ARTIFACT, CUSTOMER_INFORMATION_ARTIFACT, MARKET_ANALYSIS_ARTIFACT, \
    COMPETITORS_ARTIFACT

from src.presales_workflow_agent.sub_agent.workshop.schema.workshop_result_schema import WORKSHOP_RESULT_TEMPLATE

PRODUCT_DESIGN_PROMPT = f"""
        Your job is to analyze the results from UX and UI agents and create a comprehensive product design strategy.
        
        Follow these steps:
        1. Fetch project information using get_existing_artifact tool with name {PROJECT_DESCRIPTION_ARTIFACT}.
        2. Gather the UX and UI workshops outputs using get_existing_artifact tool:
           - {UX_WORKSHOP_ARTIFACT}
           - {UI_WORKSHOP_ARTIFACT}
           
        3. Also gather additional context using get_existing_artifact tool:
           - {CUSTOMER_INFORMATION_ARTIFACT}
           - {MARKET_ANALYSIS_ARTIFACT}
           - {COMPETITORS_ARTIFACT}
        
        4. If necessary, use knowledge_base_remote_agent_tool to search for any relevant previous experience 
           the company has with similar product designs.
        
        5. Analyze whether this project requires product design work based on the outputs from UX and UI agents.
           If both UX and UI agents determined that their areas are not applicable, then produce a summary
           indicating that product design is not required with appropriate explanation.
        
        6. Based on the information, create a comprehensive product design strategy that:
           - Integrates the UX and UI recommendations into a cohesive product vision
           - Resolves any conflicts or inconsistencies between UX and UI recommendations
           - Defines the product's value proposition and unique selling points
           - Outlines the product's core features and functionalities
           - Establishes design principles and brand guidelines
           - Creates realistic project estimations for the entire product design phase
           - Identifies product design assumptions
           - Lists product design risks with mitigation strategies
        
        7. Your product design strategy should include:
           - Executive summary of the product vision
           - User-centered design approach
           - Core user journeys and experiences
           - Product design system and component strategy
           - Visual identity guidelines
           - Design-to-development handoff process
           - Prototyping and testing strategy
           - Design quality assurance approach
           - Timeline and milestone recommendations
           - Team composition recommendations
           
        8. Create a summary and save results using save_artifact tool with name {PRODUCT_DESIGN_WORKSHOP_ARTIFACT} in format {WORKSHOP_RESULT_TEMPLATE}
    """