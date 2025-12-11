from fastapi import APIRouter,Depends
from models.order_items import OrderItems
from models.foods import Foods
from sqlalchemy import text
from sqlalchemy.orm import Session
from schemas.order_items import OrderItemSchema
from dependencies import connect_to_db
from db.database import create_engine


order_item_router=APIRouter(prefix="/order_items",tags=["OrderItem_Details"])

@order_item_router.get("/{order_id}")
def get_all_order_items(order_id: int, dbs: Session = Depends(connect_to_db)):
    raw_query = f"""SELECT
    order_items.food_id,
    foods.food_name,
    foods.price,
    order_items.qty
        FROM order_items
        JOIN foods
        ON foods.food_id = order_items.food_id
        WHERE order_items.order_id = {order_id}
        ;"""
    all_items = dbs.execute(text(raw_query))
    result = []
    for food_id, food_name, price, qty in all_items:
        temp = {"food_id": food_id, "food_name": food_name, "price": price, "qty": qty}
        result.append(temp)
    return result

@order_item_router.post("/")
def create_order_item(new_order_item:OrderItemSchema,dbs:Session=Depends(connect_to_db)):
    new_entry=OrderItems(
        order_id=new_order_item.order_id,
        qty=new_order_item.qty,
        food_id=new_order_item.food_id
    )

    dbs.add(new_entry)
    dbs.commit()
    dbs.refresh(new_entry)
    return new_entry



