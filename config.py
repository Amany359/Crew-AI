import os
from dotenv import load_dotenv
from crewai import LLM

load_dotenv()  # ده مهم عشان يقرا .env

llm = LLM(
    model="gemini/gemini-2.0-flash",
    api_key=os.getenv("GEMINI_API_KEY"),  # هنا استخدمنا الاسم الجديد
    temperature=0
)
