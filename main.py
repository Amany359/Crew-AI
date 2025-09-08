import os
from dotenv import load_dotenv
from crewai import Crew, Process, Task
from crewai.llm import LLM

# تحميل المتغيرات من ملف .env
load_dotenv()

# قراءة مفتاح Gemini API
gemini_key = os.getenv("GEMINI_API_KEY")
if not gemini_key:
    raise ValueError("❌ لم يتم العثور على GEMINI_API_KEY في البيئة أو ملف .env")

# إنشاء LLM باستخدام Gemini وربطه بمفتاح API
llm = LLM(model="gemini/gemini-1.5-flash", api_key=gemini_key)

# استيراد الـ agents
from agents.writer_agent import writer_agent
from agents.summarizer_agent import summarizer_agent
from agents.fact_checker_agent import fact_checker_agent
from agents.metadata_agent import metadata_agent

# ربط كل agent بالـ LLM
writer_agent.llm = llm
summarizer_agent.llm = llm
fact_checker_agent.llm = llm
metadata_agent.llm = llm

# تعريف المهام لمقال عن Crew AI
writer_task = Task(
    description="اكتب مقالًا مفصلًا باللغة العربية عن Crew AI، يشرح ما هو، مميزاته، وكيفية استخدامه.",
    agent=writer_agent,
    expected_output="مقال باللغة العربية عن Crew AI"
)

summarizer_task = Task(
    description="لخص المقال المكتوب في 3 جمل قصيرة وواضحة.",
    agent=summarizer_agent,
    expected_output="ملخص من 3 جمل"
)

fact_checker_task = Task(
    description="تحقق من أن جميع الحقائق المذكورة في المقال دقيقة.",
    agent=fact_checker_agent,
    expected_output="تقرير عن الحقائق الصحيحة أو المغلوطة"
)

metadata_task = Task(
    description="ولد كلمات مفتاحية مرتبطة بالمقال لتحسين SEO.",
    agent=metadata_agent,
    expected_output="قائمة كلمات مفتاحية (SEO)"
)

# إنشاء الـ Crew وربط المهام
crew = Crew(
    agents=[writer_agent, summarizer_agent, fact_checker_agent, metadata_agent],
    tasks=[writer_task, summarizer_task, fact_checker_task, metadata_task],
    process=Process.sequential,
    verbose=True
)

if __name__ == "__main__":
    result = crew.kickoff()
    print("\n=== النتيجة النهائية ===")
    print(result)
