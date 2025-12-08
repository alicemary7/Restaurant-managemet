from pydantic import BaseModel

class Restaurant_schema(BaseModel):
    name:str
    location:str
    status:bool