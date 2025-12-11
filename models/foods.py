from sqlalchemy import Column,Integer,String,Boolean,ForeignKey
from sqlalchemy.orm import relationship


from db.database import Base

class Foods(Base):
    __tablename__="foods"

    food_id=Column(Integer,primary_key=True)
    price=Column(Integer)
    food_name=Column(String)
    qty=Column(Integer)
    availability=Column(Boolean)
    res_id=Column(Integer,ForeignKey("restaurant.res_id"))
    restaurant=relationship("Restaurant")




