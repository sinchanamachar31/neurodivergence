import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

def tutor_interaction(concept, student_answer):

    prompt = f"""
You are an adaptive AI tutor.

Concept:
{concept}

Student answer:
{student_answer}

Your task:

1. Evaluate if the student answer is correct.
2. If correct → congratulate and give next small insight.
3. If partially correct → clarify misunderstanding.
4. If wrong → explain the concept again simply.

Respond in JSON:

{{
"evaluation": "",
"feedback": "",
"next_step": ""
}}
"""

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "openai/gpt-4o-mini",
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }
    )

    return response.json()["choices"][0]["message"]["content"]