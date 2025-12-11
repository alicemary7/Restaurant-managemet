from fastapi import FastAPI
from routers.foods import food_router
from routers.restaurant import restaurant_router
from db.database import Base,engine
from routers.user import user_router
from routers.order import order_router
from routers.order_items import order_item_router

Base.metadata.create_all(bind=engine)

app=FastAPI()



# decorater function

@app.get("/")
def greet():
    return {"message":"Welcome to server"}


app.include_router(food_router)
app.include_router(restaurant_router)
app.include_router(user_router)
app.include_router(order_router)
app.include_router(order_item_router)
