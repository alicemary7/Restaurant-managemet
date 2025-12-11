from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import relationship
from db.database import Base
class Users(Base):

    __tablename__="customers"
    user_id=Column(Integer,primary_key=True,index=True)
    user_name=Column(String)
    city=Column(String)
    email=Column(String)
    # orders=relationship("Orders")


