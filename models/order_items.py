from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base

class OrderItems(Base):
    __tablename__ = "order_items"

    order_items_id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("orders.order_id"))
    qty = Column(Integer)
    food_id = Column(Integer, ForeignKey("foods.food_id"))

    order = relationship("Orders")
    food = relationship("Foods")
