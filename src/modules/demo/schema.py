from pydantic import BaseModel

class AddUserSchema(BaseModel):
    name:str
    email:str