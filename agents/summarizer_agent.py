from crewai import Agent
from config import llm
summarizer_agent = Agent(
    role="Summarizer",
    goal="تلخيص النصوص الطويلة",
    backstory="خبير في تبسيط المحتوى وتقديمه في شكل ملخص",
    llm="gpt-4o-mini",
    verbose=True
)
