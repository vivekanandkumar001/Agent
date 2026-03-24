
from app.agents.research_agent import research
from app.agents.engineer_agent import generate_code
from app.agents.devops_agent import deploy_plan

def run_pipeline(idea):

    research_report = research(idea)

    code = generate_code(research_report)

    deployment = deploy_plan(code)

    return {
        "research": research_report,
        "code": code,
        "deployment": deployment
    }
