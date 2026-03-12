import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")


def generate_flashcards(concept):

    prompt = f"""
    Create 5 flashcards for learning this concept.

    Concept:
    {concept}

    Format:

    Flashcard 1
    Q:
    A:
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
        return "Flashcard generation failed"

    return data["choices"][0]["message"]["content"]