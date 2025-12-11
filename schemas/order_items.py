from pydantic import BaseModel

class OrderItemSchema(BaseModel):
    order_id:int
    qty:int
    food_id:int

