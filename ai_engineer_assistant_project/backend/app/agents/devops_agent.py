
import google.generativeai as genai, os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def deploy_plan(code):

    model = genai.GenerativeModel("gemini-pro")

    prompt = f"""
Create deployment instructions for this project.

Include:
Docker
Cloud deployment
CI/CD
"""

    response = model.generate_content(prompt)

    return response.text
