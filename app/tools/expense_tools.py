import requests
from langchain.tools import BaseTool

class ExpenseReportTool(BaseTool):
    name = "Expense Report Tool"
    description = "Fetches expense reports via FastAPI."

    def _run(self, query: str):
        # Extract user ID (person_id) from query
        user_id = extract_user_id(query)
        
        if not user_id:
            return {"error": "Failed to extract user ID from the query."}
        
        # Fetch expense report from FastAPI
        response = requests.get(f'http://localhost:8000/get-expense-report/{user_id}')
        return response.text  # CSV response

# Function to extract user_id for expense report or analysis
def extract_user_id(query: str):
    import re
    user_id = re.search(r"user ID (\d+)", query)
    if user_id:
        return user_id.group(1)
    return None
