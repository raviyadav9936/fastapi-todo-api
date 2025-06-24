from fastapi import APIRouter,Depends
from database.database import get_db
from modules.auth.crud import login_user
from modules.auth.schema import UserLogin
from sqlalchemy.orm import Session
from typing import Annotated
from modules.auth.oauth import JWTBearer

user_depndency=Annotated[dict,Depends(JWTBearer())]

router=APIRouter(prefix='/user_auth')

@router.post('/login',)
def login(request: UserLogin, db: Session = Depends(get_db)):
    return login_user(request, db)
    





