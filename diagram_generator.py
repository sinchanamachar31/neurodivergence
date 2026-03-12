import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")


def generate_diagram(concept):

    prompt = f"""
    Convert this concept into a simple step-by-step learning diagram.

    Concept:
    {concept}

    Output format example:

    Step 1 → Step 2 → Step 3 → Step 4
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
        return "Diagram generation failed"

    return data["choices"][0]["message"]["content"]