# app/planner.py

from app.model import get_llm_plan

def plan_from_query(query: str):
    return get_llm_plan(query)
