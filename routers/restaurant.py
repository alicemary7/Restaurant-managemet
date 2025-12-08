from fastapi import APIRouter, Depends

# schema
from schemas.restaurant import Restaurant_schema
from dependencies import connect_to_db
from sqlalchemy.orm import Session

from models.restaurant import Restaurant


restaurant_router= APIRouter(prefix="/restaurant",tags=["Restaurant"]) 


@restaurant_router.get("/all_restaurant")
def get_all_restaurant(dbs:Session=Depends(connect_to_db)):
    get_all_restaurant=dbs.query(Restaurant).all()
    return get_all_restaurant

@restaurant_router.get("/specific_id{id}")
def get_restaurant_byid(id:int,dbs:Session=Depends(connect_to_db)):
    particular_restaurant=dbs.query(Restaurant).filter(Restaurant.id==id).first()
    if not particular_restaurant:
        return {"message":"Invalid ID"}
    return particular_restaurant


@restaurant_router.post("/add_restaurant")
def add_restaurant(new_restaurant:Restaurant_schema,dbs:Session=Depends(connect_to_db)):
    new_entry=Restaurant(
        name=new_restaurant.name,
        location=new_restaurant.location,
        status=new_restaurant.status
    )

    
    dbs.commit()
    dbs.refresh(new_entry)
    return {"message":"added successfully"}

@restaurant_router.put("/update_restaurant/{id}")
def update_restaurant(id:int,new_restaurant:Restaurant_schema,dbs:Session=Depends(connect_to_db)):
    update_entry=dbs.query(Restaurant).filter(Restaurant.id==id).first()
    if not update_entry:
        return {"message":"Invalid ID"}
    
    update_entry.name=new_restaurant.name,
    update_entry.location=new_restaurant.location,
    update_entry.status=new_restaurant.status

    dbs.commit()
    dbs.refresh(update_entry)
    return {"message":"updated successfully"}
    

@restaurant_router.delete("/delete_restaurant/{id}")
def delete_restaurant(id:int,new_restaurant:Restaurant_schema,dbs:Session=Depends(connect_to_db)):
    delete_entry=dbs.query(Restaurant).filter(Restaurant.id==id).first()
    if not delete_restaurant:
        return {"message":"Invalid ID"}
    
    
    dbs.delete(delete_entry)
    dbs.commit()
    return {"message":"deleted successfully"}
    
