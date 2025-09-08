from crewai import Agent
from config import llm
fact_checker_agent = Agent(
    role="Fact Checker",
    goal="التحقق من صحة المعلومات",
    backstory="خبير في مراجعة الحقائق",
    llm="gpt-4o-mini",
    verbose=True
)
