from fastapi import FastAPI
from routers.foods import food_router
from routers.restaurant import restaurant_router
from db.database import Base,engine

Base.metadata.create_all(bind=engine)

app=FastAPI()



# decorater function

@app.get("/")
def greet():
    return {"message":"Welcome to server"}
app.include_router(food_router)
app.include_router(restaurant_router)
