from fastapi import Depends,HTTPException
from sqlalchemy.orm import Session
from database.models import User
from modules.auth.oauth import Hash,create_access_token


def login_user(request, db: Session):
    user = db.query(User).filter(User.user_name == request.user_name).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if not Hash.verify(request.password, user.password):
        raise HTTPException(status_code=400, detail="Incorrect password")
    
    access_token = create_access_token({"sub": user.user_name})
    return {"access_token": access_token, "token_type": "bearer"}