from crewai import Crew, Process
from agents import author_agent, summarizer_agent
from tasks import generate_task, summarizer_task

# إعداد الـ Crew
crew = Crew(
    agents=[author_agent, summarizer_agent],
    tasks=[generate_task, summarizer_task],
    process=Process.sequential
)
