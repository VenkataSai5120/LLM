import requests
from langchain.tools import BaseTool
from datetime import datetime

class MeetingCreateTool(BaseTool):
    name = "Meeting Create Tool"
    description = "Creates a meeting via FastAPI."

    def _run(self, query: str):
        # Extract meeting details from the query using a helper function
        meeting_data = extract_meeting_details(query)
        
        if not meeting_data:
            return {"error": "Failed to extract meeting details from the query."}
        
        # Send data to FastAPI meeting creation endpoint
        response = requests.post('http://localhost:8000/create-meeting', json=meeting_data)
        return response.json()

# Function to extract meeting details
def extract_meeting_details(query: str):
    import re
    meeting_name = re.search(r"called '([^']+)'", query)
    user_id = re.search(r"user ID (\d+)", query)
    start_time = re.search(r"from ([\d:]+ [APM]+)", query)
    end_time = re.search(r"to ([\d:]+ [APM]+)", query)
    
    if meeting_name and user_id and start_time and end_time:
        start_time = datetime.strptime(start_time.group(1), "%I:%M %p")
        end_time = datetime.strptime(end_time.group(1), "%I:%M %p")
        
        return {
            "meeting_name": meeting_name.group(1),
            "user_id": int(user_id.group(1)),
            "start_time": start_time,
            "end_time": end_time
        }
    return None
