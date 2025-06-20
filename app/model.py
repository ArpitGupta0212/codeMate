# app/model.py

import subprocess
import json
from app.function_lib import function_library

def load_prompt(query: str) -> str:
    with open("app/prompt_template.txt") as f:
        template = f.read()
    function_desc = "\n".join([f"{k}: {v['description']}" for k, v in function_library.items()])
    return template.format(function_list=function_desc, user_query=query)

def get_llm_plan(query: str):
    prompt = load_prompt(query)
    response = subprocess.run(
        ["ollama", "run", "mistral"], 
        input=prompt,
        capture_output=True,
        text=True
    )
    try:
        return json.loads(response.stdout)
    except Exception as e:
        return {"error": "Invalid JSON returned", "raw_output": response.stdout}
