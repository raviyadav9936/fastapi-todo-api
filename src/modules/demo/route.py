from modules.demo.crud import show_user,index,create_user,get_data
from fastapi import APIRouter,Depends
from database.database import get_db
from sqlalchemy.orm import Session
from modules.demo.schema import AddUserSchema

router=APIRouter(prefix='/user_record')

@router.get('/user')
def show_user():
    return show_user()

@router.get('/index')
def show_index(id:int):
    return index(id)

@router.post('/add_user')
def add_data(schema:AddUserSchema,db:Session=Depends(get_db)):
    print('--',db)
    res= create_user(schema,db)
    return res

@router.get('/get_user_data')
def user_data(db:Session=Depends(get_db)):
    res=get_data(db)
    return res