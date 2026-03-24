
from fastapi import FastAPI
from app.orchestrator.workflow import run_pipeline
from dotenv import load_dotenv
load_dotenv()
app = FastAPI(title="AI Engineering Assistant")

@app.get("/")
def health():
    return {"status": "running"}

@app.post("/build")
async def build_project(data: dict):
    idea = data.get("idea")
    result = run_pipeline(idea)
    return result
