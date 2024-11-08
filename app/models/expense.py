from pydantic import BaseModel

class Expense(BaseModel):
    expense_id: int
    user_id: int
    order_id: int
    expense_amount: float
    category: str
