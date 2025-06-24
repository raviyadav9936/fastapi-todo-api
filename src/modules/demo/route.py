from modules.demo.crud import create_user,get_data,update_record,delete_record,get_data_with_id
from fastapi import APIRouter,Depends
from database.database import get_db
from sqlalchemy.orm import Session
from modules.demo.schema import AddUserSchema,UpdateSchema 
from modules.auth.oauth import JWTBearer
from typing import Annotated

router=APIRouter(
    prefix='/user_record'
)
user_depndency=Annotated[dict,Depends(JWTBearer())]

@router.post('/add_user')
def add_data(schema:AddUserSchema,db:Session=Depends(get_db)):
    res= create_user(schema,db)
    return res

@router.get('/get_user_data')
def user_data(user:user_depndency,db:Session=Depends(get_db)):
    res=get_data(db)
    return res

@router.get('/get_record')
def fetch_record_id(user:user_depndency,id:int,db:Session=Depends(get_db)):
    res=get_data_with_id(id,db)
    return res

@router.put('/update_user')
def update_user(id:int,schema:UpdateSchema,db:Session=Depends(get_db)):
    res=update_record(id,schema,db)
    return res

@router.delete('/delete_user')
def delete_user(id:int,db:Session=Depends(get_db)):
    res=delete_record(id,db)
    return res