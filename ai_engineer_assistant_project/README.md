
# AI Engineering Assistant

Autonomous multi-agent AI engineering system.

## Features
- Idea research (Claude)
- Code generation (OpenAI)
- DevOps planning (Gemini)

## Run Backend

cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload

## Run Dashboard

streamlit run dashboard/streamlit_dashboard.py

## Frontend

Use Next.js and connect to API at localhost:8000/build
