
# memory.py

"""
This file manages TrendPilot's memory.
It stores previous topics, platforms, tones, and generated outputs.
"""

import json
import os
from datetime import datetime


# Memory file location
MEMORY_FILE = "outputs/saved_results/memory.json"


# Create memory file if it does not exist
def initialize_memory():

    os.makedirs(os.path.dirname(MEMORY_FILE), exist_ok=True)

    if not os.path.exists(MEMORY_FILE):

        with open(MEMORY_FILE, "w", encoding="utf-8") as file:
            json.dump([], file, indent=4)


# Load previous memory
def load_memory():

    initialize_memory()

    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except (json.JSONDecodeError, OSError):
        return []


# Save a new generated result
def save_memory(topic, platform, tone, output):

    print("[MEMORY] Saving generated content...")

    memory = load_memory()

    new_record = {
        "topic": topic,
        "platform": platform,
        "tone": tone,
        "output": output,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    memory.append(new_record)

    with open(MEMORY_FILE, "w", encoding="utf-8") as file:

        json.dump(
            memory,
            file,
            indent=4,
            ensure_ascii=False
        )

    print("[MEMORY] Content saved successfully.")

    return new_record


# Retrieve previous generated results
def get_previous_results():

    print("[MEMORY] Retrieving previous results...")

    return load_memory()


# Get the latest generated result
def get_latest_result():

    memory = load_memory()

    if not memory:
        return None

    return memory[-1]
