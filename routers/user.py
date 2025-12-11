from fastapi import APIRouter,Depends
from models.user import Users
from sqlalchemy.orm import Session
from schemas.user import UserSchemas
from dependencies import connect_to_db
from db.database import create_engine

user_router=APIRouter(prefix="/users",tags=["UserDetails"])

@user_router.get("/")
def all_user_details(dbs:Session=Depends(connect_to_db)):
    all_user=dbs.query(Users).all()
    return all_user

@user_router.post("/all_user")
def user_details(new_user:UserSchemas,dbs:Session=Depends(connect_to_db)):
    new_entry=Users(
        user_name=new_user.user_name,
        city=new_user.city,
        email=new_user.email
    )
    dbs.add(new_entry)
    dbs.commit()
    dbs.refresh(new_entry)
    return {"message":"added successfully"}

@user_router.get("/by_id/{id}")
def user_details(id:int,dbs:Session=Depends(connect_to_db)):
    single_entry=dbs.query(Users).filter(Users.user_id==id).first()
    if not single_entry:
        return {"message":"Invalid ID"}
    return single_entry

@user_router.put("/update_user/{id}")
def update_user(id:int,new_user:UserSchemas,dbs:Session=Depends(connect_to_db)):
    update_entry=dbs.query(Users).filter(Users.user_id==id).first()
    if not update_entry:
        return {"message":"Invalid ID"}
    
    update_entry.user_name=new_user.user_name,
    update_entry.email=new_user.email,
    update_entry.city=new_user.city

    dbs.commit()
    dbs.refresh(update_entry)
    return {"message":"updated successfully"}

@user_router.delete("/delete_user/{id}")
def delete_user(id:int,dbs:Session=Depends(connect_to_db)):
    delete_entry=dbs.query(Users).filter(Users.user_id==id).first()
    if not delete_entry:
        return {"message":"Invalid ID"}
    dbs.delete(delete_entry)
    dbs.commit()
    return {"message":"deleted successfully"}


