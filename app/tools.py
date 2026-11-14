
# tools.py

"""
This file contains the tools used by the TrendPilot AI Agent.
Each tool performs a specific content-generation task using Ollama.
"""

import requests
import os
from datetime import datetime

from app.prompts import SYSTEM_PROMPT, REVIEW_PROMPT, build_content_prompt


# Ollama configuration
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "gemma3:4b"


# Connect with local Ollama model
def ask_ollama(prompt):

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False,
        "options": {
            "num_predict": 900
        }
    }

    response = requests.post(
        OLLAMA_URL,
        json=payload,
        timeout=300
    )

    response.raise_for_status()

    return response.json()["response"]
# TOOL 1: Trend Idea Generator
def trend_idea_generator(topic, platform):

    print("[TOOL USED] Trend Idea Generator")

    prompt = f"""
{SYSTEM_PROMPT}

Generate 5 creative content ideas about:

Topic: {topic}
Platform: {platform}

For each idea, explain why it could engage the audience.
Do not guarantee viral performance.
"""

    return ask_ollama(prompt)


# TOOL 2: Caption Writer
def caption_writer(topic, platform, tone):

    print("[TOOL USED] Caption Writer")

    prompt = f"""
Write an engaging social media caption.

Topic: {topic}
Platform: {platform}
Tone: {tone}

Requirements:
- Start with an attractive hook.
- Explain the topic clearly.
- Use suitable formatting.
- End with an engaging call to action.
- Do not invent facts.
"""

    return ask_ollama(prompt)


# TOOL 3: Hashtag Generator
def hashtag_generator(topic, platform):

    print("[TOOL USED] Hashtag Generator")

    prompt = f"""
Generate 10 relevant hashtags.

Topic: {topic}
Platform: {platform}

Requirements:
- Use relevant hashtags only.
- Include a mixture of broad and specific hashtags.
- Avoid irrelevant trending tags.
- Return hashtags in a clean list.
"""

    return ask_ollama(prompt)


# TOOL 4: Reel Script Generator
def reel_script_generator(topic, tone):

    print("[TOOL USED] Reel Script Generator")

    prompt = f"""
Create a 30-60 second short video script.

Topic: {topic}
Tone: {tone}

Include:
1. Opening hook
2. Main explanation
3. Visual suggestions
4. Closing line

Keep the script engaging and easy to understand.
Do not invent project results.
"""

    return ask_ollama(prompt)


# TOOL 5: Content Reviewer
def content_reviewer(content, platform, tone):

    print("[TOOL USED] Content Reviewer")

    prompt = f"""
{REVIEW_PROMPT}

Platform: {platform}
Tone: {tone}

CONTENT TO REVIEW:

{content}

Provide specific improvements.
"""

    return ask_ollama(prompt)


# TOOL 6: File Saver (Mandatory)
def file_saver(content, folder="outputs/saved_results"):

    print("[TOOL USED] File Saver")

    os.makedirs(folder, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"trendpilot_{timestamp}.md"

    file_path = os.path.join(folder, filename)

    with open(file_path, "w", encoding="utf-8") as file:

        file.write("# TrendPilot Generated Content\n\n")
        file.write(content)

    return file_path




# TOOL 7: Complete Content Generator
def complete_content_generator(topic, platform, tone, output_type):

    print("[TOOL USED] Complete Content Generator")

    prompt = build_content_prompt(
        topic,
        platform,
        tone,
        output_type
    )

    return ask_ollama(prompt)


