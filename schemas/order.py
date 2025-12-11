from pydantic import BaseModel

class OrderSchemas(BaseModel):
    user_id: int
    res_id: int
    total_amount: float
