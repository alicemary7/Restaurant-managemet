from fastapi import APIRouter,Depends
from models.order import Orders
from sqlalchemy.orm import Session
from schemas.order import OrderSchemas
from dependencies import connect_to_db
from db.database import create_engine

order_router=APIRouter(prefix="/orders",tags=["OrderDetails"])

@order_router.get("/orders")
def get_orders(db: Session = Depends(connect_to_db)):
    return db.query(Orders).all()


@order_router.get("/orders/{order_id}")
def get_order(order_id: int, db: Session = Depends(connect_to_db)):
    return db.query(Orders).filter(Orders.order_id == order_id).first()


@order_router.post("/orders/create")
def create_order(order: OrderSchemas, db: Session = Depends(connect_to_db)):
    new_order = Orders(
        user_id=order.user_id,
        res_id=order.res_id,
        total_amount=order.total_amount
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order