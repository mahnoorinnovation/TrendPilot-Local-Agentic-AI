
# main.py

"""
TrendPilot - Local Agentic AI Assistant
Main entry point of the application.
"""

from app.agent import TrendPilotAgent


def main():

    print("\n======================================")
    print("       WELCOME TO TRENDPILOT")
    print("    Your Local AI Content Assistant")
    print("======================================")

    print("\nPlease provide the following details.")

    # Get user inputs
    topic = input("\nEnter your content topic: ").strip()

    platform = input(
        "Enter platform (Instagram/LinkedIn/YouTube/X/Facebook): "
    ).strip()

    tone = input(
        "Enter content tone (Professional/Casual/Friendly): "
    ).strip()

    output_type = input(
        "Enter output type (Post/Reel/Complete Plan): "
    ).strip()

    try:

        # Initialize agent
        agent = TrendPilotAgent()

        # Execute agent workflow
        result = agent.run(
            topic,
            platform,
            tone,
            output_type
        )

        # Display final result
        print("\n======================================")
        print("          FINAL AI OUTPUT")
        print("======================================")

        print(result["content"])

        print("\nYour content has been saved successfully!")
        print("Saved file:", result["saved_file"])

    except Exception as error:

        print("\n[ERROR] Something went wrong.")
        print("Details:", error)


if __name__ == "__main__":
    main()
