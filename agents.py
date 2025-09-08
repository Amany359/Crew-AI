from crewai import Agent, LLM
from dotenv import load_dotenv
import os

# تحميل المتغيرات من .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("❌ GEMINI_API_KEY not found in .env file")

# إعداد الـ LLM
llm = LLM(
    model="gemini/gemini-2.0-flash",
   temperature=0,
)

# Agent 1: Author
author_agent = Agent(
    role="Author",
    goal="Generate stories given some details",
    backstory="German author with 5 years experience inspired by Ahmed Khaled Tawfiq",
    llm=llm,
    verbose=True
)

# Agent 2: Summarizer
summarizer_agent = Agent(
    role="Summarizer",
    goal="Summarize stories",
    backstory="American author with 5 years experience",
    llm=llm,
    verbose=True
)
