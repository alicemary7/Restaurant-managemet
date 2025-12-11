
from sqlalchemy import Column,Integer,String,ForeignKey,Float
from sqlalchemy.orm import relationship

from db.database import Base
class Orders(Base):
    __tablename__="orders"

    order_id=Column(Integer,primary_key=True)
    user_id=Column(Integer,ForeignKey("customers.user_id"))
    res_id=Column(Integer,ForeignKey("restaurant.res_id"))
    total_amount=Column(Float)


    users=relationship("Users")
    restaurants=relationship("Restaurant")

    
