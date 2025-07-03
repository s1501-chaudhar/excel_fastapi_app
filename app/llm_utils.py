import os
import requests
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

SYSTEM_PROMPT = """
You are an AI assistant with access to the following Excel data tables: Initial Investment, Revenue Projections, and Operating Expenses. Answer questions in plain English based on the provided Excel file.
"""

def ask_question(prompt: str):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "mixtral-8x7b-32768",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ]
    }
    response = requests.post(GROQ_URL, json=data, headers=headers)
    result = response.json()
    return {"response": result["choices"][0]["message"]["content"]}