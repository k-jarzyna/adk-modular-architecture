from src.shared.artifact.artifact_definition import UX_WORKSHOP_ARTIFACT, PROJECT_DESCRIPTION_ARTIFACT, \
    CUSTOMER_INFORMATION_ARTIFACT, MARKET_ANALYSIS_ARTIFACT, COMPETITORS_ARTIFACT, OF_THE_SHELF_SOLUTIONS_ARTIFACT, \
    COMPANY_EXPERIENCE_ARTIFACT

from src.presales_workflow_agent.sub_agent.workshop.schema.workshop_result_schema import WORKSHOP_RESULT_TEMPLATE

UX_PROMPT = f"""
        Your job is to analyze the presales information from a UX designer's perspective and provide UX-related insights and recommendations.
        
        Follow these steps:
        1. Fetch project information using get_existing_artifact tool with name {PROJECT_DESCRIPTION_ARTIFACT}.
        2. Gather additional context using get_existing_artifact tool for the following artifacts:
           - {CUSTOMER_INFORMATION_ARTIFACT}
           - {MARKET_ANALYSIS_ARTIFACT}
           - {COMPETITORS_ARTIFACT}
           - {OF_THE_SHELF_SOLUTIONS_ARTIFACT}
           - {COMPANY_EXPERIENCE_ARTIFACT}
        
        3. If necessary, use knowledge_base_remote_agent_tool to search for any relevant previous experience 
           the company has with similar UX designs, user research, or usability testing.
        
        4. Assess if this project actually requires UX design work. 
           If you determine that UX design is not applicable to this project, 
           create a summary indicating that and save it as a result with appropriate explanation.
        
        5. Based on the information, perform a comprehensive UX analysis:
           - Create realistic project estimations for UX work (min/max)
           - Identify UX-specific project assumptions
           - List recommended UX tools, methodologies, and frameworks
           - Identify UX-related risks with impact, probability and mitigation strategies
        
        6. Ensure your analysis includes:
           - User research recommendations
           - Information architecture considerations
           - Usability testing approach
           - Accessibility requirements
           - User personas and user journey recommendations
           - Interaction design considerations
           - Mobile/responsive design needs
           
        7. Create a summary and save results using save_artifact tool with name {UX_WORKSHOP_ARTIFACT} in format: {WORKSHOP_RESULT_TEMPLATE}
    """