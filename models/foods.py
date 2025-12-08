from sqlalchemy import Column,Integer,String,Boolean

from db.database import Base

class Foods(Base):
    __tablename__="food"

    food_id=Column(Integer,primary_key=True)
    price=Column(Integer)
    food_name=Column(String)
    qty=Column(Integer)
    availability=Column(Boolean)

