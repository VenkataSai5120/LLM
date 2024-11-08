from pydantic import BaseModel
from datetime import datetime

class Meeting(BaseModel):
    meeting_id: int
    meeting_name: str
    user_id: int
    start_time: datetime
    end_time: datetime
