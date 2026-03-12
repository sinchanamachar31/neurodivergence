import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")


def generate_worksheet(concept):

    prompt = f"""
    Generate a practice worksheet for this concept.

    Include:
    - 3 MCQs
    - 2 short answer questions
    - 1 application question

    Concept:
    {concept}
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

    data = response.json()

    if "choices" not in data:
        return "Worksheet generation failed"

    return data["choices"][0]["message"]["content"]