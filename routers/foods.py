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


# POST
@food_router.post("/")
def get_all_foods(new_food: Foods_schema, dbs: Session = Depends(connect_to_db)):

    some_food_name = new_food.food_name
    some_price = new_food.price
    some_qty = new_food.qty
    something_avl = new_food.availability
    # food new model
    new_entry = Foods(
        food_name=some_food_name,
        price=some_price,
        qty=some_qty,
        availability=something_avl,
    )

    # adding the row
    dbs.add(new_entry)
    # committing the row
    dbs.commit()
    # refresh the table
    dbs.refresh(new_entry)
    return {"message":"added successfully"}



# update

@food_router.put("/{food_id}")
def update_food(food_id:int,new_food:Foods_schema,dbs:Session=Depends(connect_to_db)):
    update_entry= dbs.query(Foods).filter(Foods.food_id==food_id).first()

    update_entry.food_name=new_food.food_name,
    update_entry.price=new_food.price,
    update_entry.qty=new_food.qty,
    update_entry.availability=new_food.availability

    
    dbs.commit()
    dbs.refresh(update_entry)
    return {"message":"updated successfully"}


# delete

@food_router.delete("/{food_id}")
def delete_food(food_id:int,new_food:Foods_schema,dbs:Session=Depends(connect_to_db)):
    delete_entry=dbs.query(Foods).filter(Foods.food_id==food_id).first()

    dbs.delete(delete_entry)
    dbs.commit()
    return {"message":"deleted successfully"}
