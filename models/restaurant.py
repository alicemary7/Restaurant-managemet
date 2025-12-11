from sqlalchemy import Column,Integer,String,Boolean



from db.database import Base

class Restaurant(Base):
    __tablename__="restaurant"

    res_id=Column(Integer,primary_key=True)
    name=Column(String)
    location=Column(String)
    status=Column(Boolean)

   