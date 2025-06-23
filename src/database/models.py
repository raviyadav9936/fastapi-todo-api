from sqlalchemy import Integer,String,Column,Boolean,TIMESTAMP, func
from database.database import Base

class User(Base):
    __tablename__ ='users'
    
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(50))
    email=Column(String(100))
    tstatus=Column(Boolean,default=True)
    created_at=Column(TIMESTAMP,server_default=func.now())
    updated_at=Column(TIMESTAMP)
