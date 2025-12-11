from pydantic import BaseModel

class UserSchemas(BaseModel):
   
    user_name:str
    email:str
    city:str
