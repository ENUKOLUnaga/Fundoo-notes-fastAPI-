from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from utils.db_dependency import SessionLocal,get_db
from schemas.schema_user import UserCreate, UserUpdate
from services.user_service import (
    create_user,
    get_users,
    get_user,
    update_user,
    delete_user
)
from utils.loggers import logger

router = APIRouter(prefix="/users", tags=["Users"])


#CREATE
@router.post("/")
def register(user: UserCreate, db: Session = Depends(get_db)):
    logger.info("API called: Create User")
    return create_user(db, user)


#READ ALL
@router.get("/")
def read_users(db: Session = Depends(get_db)):
    logger.info("API called: Get Users")
    return get_users(db)


#READ ONE
@router.get("/{id}")
def read_user(id: int, db: Session = Depends(get_db)):
    logger.info(f"API called: Get User {id}")
    return get_user(db, id)


#UPDATE
@router.put("/{id}")
def update(id: int, user: UserUpdate, db: Session = Depends(get_db)):
    logger.info(f"API called: Update User {id}")
    return update_user(db, id, user)


#DELETE
@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    logger.info(f"API called: Delete User {id}")
    return delete_user(db, id)