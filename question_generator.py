import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")


def generate_question(concept):

    prompt = f"""
    Generate one simple question to test understanding of this concept:

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

    print("OPENROUTER RESPONSE:")
    print(data)

    if "choices" not in data:
        return "Question generation failed"

    return data["choices"][0]["message"]["content"]