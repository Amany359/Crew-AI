from crewai import Task
from agents import author_agent, summarizer_agent

# Task 1: Generate story
generate_task = Task(
    description="Generate story about {person_name} and about {subject} for non-native English speakers",
    expected_output="Maximum 10 lines of story",
    agent=author_agent
)

# Task 2: Summarize story
summarizer_task = Task(
    description="Summarize the story in a short and simple way. The summary should not exceed 2-3 sentences.",
    expected_output="Summary with maximum 20 words",
    agent=summarizer_agent
)
