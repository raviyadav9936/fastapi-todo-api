from pydantic import BaseModel

class AddUserSchema(BaseModel):
    name:str
    email:str
    user_name:str
    password:str
    
    
class UpdateSchema(BaseModel):
    name:str
    email:str    