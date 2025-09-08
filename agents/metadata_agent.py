from crewai import Agent
from config import llm
metadata_agent = Agent(
    role="Metadata Generator",
    goal="إنشاء كلمات مفتاحية وبيانات وصفية",
    backstory="خبير SEO يساعد على تحسين محركات البحث",
    llm="gpt-4o-mini",
    verbose=True
)
