from app.tools import (
    complete_content_generator,
    content_reviewer,
    file_saver
)
from app.memory import save_memory, get_previous_results


class TrendPilotAgent:

    def __init__(self):
        print("\nTrendPilot Agent initialized successfully!")

    def create_plan(self, topic, platform, tone, output_type):

        print("\n[AGENT] Creating execution plan...")

        plan = [
            "Understand user goal",
            "Create complete content using AI",
            "Review generated content",
            "Save final output",
            "Store result in memory"
        ]

        for number, task in enumerate(plan, start=1):
            print(f"{number}. {task}")

        return plan

    def run(self, topic, platform, tone, output_type):

        print("\n====================================")
        print("       TRENDPILOT AI AGENT")
        print("====================================")

        if not all([topic.strip(), platform.strip(), tone.strip(), output_type.strip()]):
            raise ValueError("All input fields are required.")

        self.create_plan(topic, platform, tone, output_type)

        previous_results = get_previous_results()
        print(f"\n[AGENT] Previous records found: {len(previous_results)}")

        content = complete_content_generator(
            topic,
            platform,
            tone,
            output_type
        )

        review = content_reviewer(content, platform, tone)

        final_output = f"""
# TrendPilot Final Content Plan

{content}

## Content Review

{review}
"""

        saved_file = file_saver(final_output)

        save_memory(topic, platform, tone, final_output)

        print("\n====================================")
        print("       GENERATION COMPLETED")
        print("====================================")
        print(f"\nSaved file: {saved_file}")

        return {
            "topic": topic,
            "platform": platform,
            "tone": tone,
            "content": final_output,
            "review": review,
            "saved_file": saved_file
        }
