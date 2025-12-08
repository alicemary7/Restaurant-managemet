from sqlalchemy import Column,Integer,String,Boolean

from db.database import Base

class Restaurant(Base):
    __tablename__="restaurant"

    id=Column(Integer,primary_key=True,index=True)
    name=Column(String)
    location=Column(String)
    status=Column(Boolean)