from pydantic import BaseModel, Field

class User(BaseModel):
    username: str 
    email: str 
    full_name: str 
    password: str 

