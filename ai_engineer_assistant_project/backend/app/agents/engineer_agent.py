
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_code(plan):

    prompt = f"""
You are a senior software engineer.

Create a project implementation plan and example code based on:

{plan}

Include:
backend architecture
frontend
database
APIs
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content
