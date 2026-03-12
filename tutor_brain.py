import requests
import os
from dotenv import load_dotenv

from prompts import ADHD_PROMPT, DYSLEXIA_PROMPT, VISUAL_PROMPT, EXAM_PROMPT
from flowchart_generator import generate_flowchart

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

API_URL = "https://openrouter.ai/api/v1/chat/completions"


# --------------------------------
# Learning Profile Selector
# --------------------------------

def get_learning_prompt(profile):

    if profile == "ADHD":
        return ADHD_PROMPT

    elif profile == "Dyslexia":
        return DYSLEXIA_PROMPT

    elif profile == "Visual":
        return VISUAL_PROMPT

    elif profile == "Exam":
        return EXAM_PROMPT

    else:
        return "Explain the concept clearly."


# --------------------------------
# LLM API CALL
# --------------------------------

def call_llm(prompt):

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    data = response.json()

    return data["choices"][0]["message"]["content"]


# --------------------------------
# MAIN TUTOR BRAIN
# --------------------------------

def generate_lesson(text, profile):

    learning_prompt = get_learning_prompt(profile)

    prompt = f"""
You are an adaptive AI tutor designed to help neurodivergent learners.

Learning Profile:
{profile}

Teaching Instructions:
{learning_prompt}

Study Content:
{text}

Your job is to teach this concept clearly based on the learning profile.

Generate structured learning material with these sections:

1️⃣ Explanation
Explain the concept clearly.

2️⃣ Key Points
Provide bullet point summary.

3️⃣ Flowchart
Represent the concept visually using arrows like this:

Sunlight
 ↓
Leaf
 ↓
Chlorophyll
 ↓
Glucose

4️⃣ Flashcards
Create 4 flashcards in this format:

Q: Question
A: Answer

5️⃣ Mini Quiz
Create 3 quiz questions.

Ensure the response is clear and structured.
"""

    explanation = call_llm(prompt)
    flowchart=generate_flowchart(text)

    return {
        "profile": profile,
        "lesson": explanation,
        "flowchart": flowchart
    }