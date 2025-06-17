from src.shared.artifact.artifact_definition import UI_WORKSHOP_ARTIFACT, PROJECT_DESCRIPTION_ARTIFACT, \
    CUSTOMER_INFORMATION_ARTIFACT, MARKET_ANALYSIS_ARTIFACT, COMPETITORS_ARTIFACT, OF_THE_SHELF_SOLUTIONS_ARTIFACT, \
    COMPANY_EXPERIENCE_ARTIFACT

from src.presales_workflow_agent.sub_agent.workshop.schema.workshop_result_schema import WORKSHOP_RESULT_TEMPLATE

UI_PROMPT = f"""
        Your job is to analyze the presales information from a UI designer's perspective and provide UI-related insights and recommendations.
        
        Follow these steps:
        1. Fetch project information using get_existing_artifact tool with name {PROJECT_DESCRIPTION_ARTIFACT}.
        2. Gather additional context using get_existing_artifact tool for the following artifacts:
           - {CUSTOMER_INFORMATION_ARTIFACT}
           - {MARKET_ANALYSIS_ARTIFACT}
           - {COMPETITORS_ARTIFACT}
           - {OF_THE_SHELF_SOLUTIONS_ARTIFACT}
           - {COMPANY_EXPERIENCE_ARTIFACT}
        
        3. If necessary, use knowledge_base_remote_agent_tool to search for any relevant previous experience 
           the company has with similar UI designs, design systems, or visual frameworks.
        
        4. Assess if this project actually requires UI design work. 
           If you determine that UI design is not applicable to this project, 
           create a summary indicating that and save it as a result with appropriate explanation.
        
        5. Based on the information, perform a comprehensive UI analysis:
           - Create realistic project estimations for UI work (min/max)
           - Identify UI-specific project assumptions
           - List recommended UI tools, design systems, and frameworks
           - Identify UI-related risks with impact, probability, and mitigation strategies
        
        6. Ensure your analysis includes:
           - Visual design approach
           - Component library recommendations
           - Brand identity considerations
           - Responsive design requirements
           - Design system needs
           - Prototyping approach
           - Design handoff process
           - Design quality assurance strategy
           
        7. Create a summary and save results using save_artifact tool with name {UI_WORKSHOP_ARTIFACT} in format: {WORKSHOP_RESULT_TEMPLATE}
    """