from fastapi import APIRouter, Depends
# schema
from schemas.foods import Foods_schema
from dependencies import connect_to_db
from sqlalchemy.orm import Session

# database models
from models.foods import Foods


food_router = APIRouter(prefix="/foods", tags=["Foods"])


# GET
@food_router.get("/")
def get_all_foods(dbs: Session = Depends(connect_to_db)):
    all_foods = dbs.query(Foods).all()
    return all_foods


# GET {id}
@food_router.get("/{food_id}")
def get_all_foods(food_id: int, dbs: Session = Depends(connect_to_db)):
    particular_food = dbs.query(Foods).filter(Foods.food_id == food_id).first()
    if not particular_food:
        return {"message": "Invalid Id"}
    return particular_food


@food_router.post("/")
def create_food(new_food: Foods_schema, dbs: Session = Depends(connect_to_db)):
    
    new_entry = Foods(
        food_name=new_food.food_name,
        price=new_food.price,
        qty=new_food.qty,
        availability=new_food.availability,
        res_id=new_food.res_id
    )

    dbs.add(new_entry)
    dbs.commit()
    dbs.refresh(new_entry)

    return {"message": "added successfully", "data": new_entry}



# update

@food_router.put("/{id}")
def update_products(id: int, changed: Foods_schema, dbs: Session = Depends(connect_to_db)):
    food_item = dbs.query(Foods).filter(Foods.food_id == id).first()

    if not food_item:
        return {"message": "Invalid id"}

  
    if changed.qty > food_item.qty:
        return {"message": "Not enough stock"}

    food_item.qty = food_item.qty - changed.qty

  
    food_item.food_name = changed.food_name
    food_item.price = changed.price
    food_item.availability = changed.availability

    dbs.commit()
    dbs.refresh(food_item)

    return {"message": "updated", "data": food_item}


# delete

@food_router.delete("/{food_id}")
def delete_food(food_id:int,dbs:Session=Depends(connect_to_db)):
    delete_entry=dbs.query(Foods).filter(Foods.food_id==food_id).first()

    dbs.delete(delete_entry)
    dbs.commit()
    return {"message":"deleted successfully"}
