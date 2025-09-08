from crewai import Agent
from config import llm

writer_agent = Agent(
    role="Writer",
    goal="كتابة قصة قصيرة للأطفال",
    backstory="كاتب محترف للأطفال يساعد في إنتاج محتوى إبداعي",
    llm="gpt-4o-mini",  # ممكن تغيره
    verbose=True
)
