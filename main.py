from crew import crew

# تشغيل الـ Crew
if __name__ == "__main__":
    result = crew.kickoff(
        inputs={
            "person_name": "Dr Ahmed",
            "subject": "his career",
        }
    )

    print("=== Final Result ===")
    print(result)
