from fastapi import FastAPI
from database.db_connect import engine
from models.user_models import Base
from routes.routes_users import router as user_router
from routes.routes_notes import router as note_router
app=FastAPI()

#create tables
Base.metadata.create_all(bind=engine)
app.include_router(user_router)
app.include_router(note_router)
@app.get("/")
def home():
    return {"message":"Fundoo App started"}

