from fastapi import FastAPI
from pydantic import BaseModel
from app.agents.agent import process_query

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.post("/process-query")
def process_user_query(request: QueryRequest):
    response = process_query(request.query)
    return {"response": response}
