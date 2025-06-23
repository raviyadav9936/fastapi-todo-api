from modules.demo.crud import create_user,get_data,update_record,delete_record
from fastapi import APIRouter,Depends
from database.database import get_db
from sqlalchemy.orm import Session
from modules.demo.schema import AddUserSchema,UpdateSchema 

router=APIRouter(prefix='/user_record')


@router.post('/add_user')
def add_data(schema:AddUserSchema,db:Session=Depends(get_db)):
    res= create_user(schema,db)
    return res

@router.get('/get_user_data')
def user_data(db:Session=Depends(get_db)):
    res=get_data(db)
    return res

@router.put('/update_user')
def update_user(id:int,schema:UpdateSchema,db:Session=Depends(get_db)):
    res=update_record(id,schema,db)
    return res

@router.delete('/delete_user')
def delete_user(id:int,db:Session=Depends(get_db)):
    res=delete_record(id,db)
    return res