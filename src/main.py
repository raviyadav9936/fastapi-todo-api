from fastapi import FastAPI
from database.database import Base,engine
import modules.demo.route as demo
import modules.auth.route as auth

Base.metadata.create_all(bind=engine)
app=FastAPI()

app.include_router(auth.router,tags=['Login'])
app.include_router(demo.router,tags=['User'])