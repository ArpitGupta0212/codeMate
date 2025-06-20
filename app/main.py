# app/main.py

from fastapi import FastAPI
from pydantic import BaseModel
from app.planner import plan_from_query

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.post("/plan/")
def get_plan(req: QueryRequest):
    return {"plan": plan_from_query(req.query)}
