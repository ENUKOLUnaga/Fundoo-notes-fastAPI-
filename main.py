from fastapi import FastAPI
from database.db_connect import engine
from models.user_models import Base
from routes.routes_users import router as user_router
app=FastAPI()

#create tables
Base.metadata.create_all(bind=engine)
app.include_router(user_router)
@app.get("/")
def home():
    return {"message":"Fundoo App started"}

