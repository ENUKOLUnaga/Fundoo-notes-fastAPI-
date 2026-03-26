from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from utils.db_dependency import get_db
from schemas.schema_note import NoteCreate, NoteUpdate
from services.note_service import (
    create_note,
    get_notes,
    get_notes_by_user,
    update_note,
    delete_note
)

router = APIRouter(prefix="/notes", tags=["Notes"])


@router.post("/")
def create(note: NoteCreate, db: Session = Depends(get_db)):
    return create_note(db, note)


@router.get("/")
def read_all(db: Session = Depends(get_db)):
    return get_notes(db)


@router.get("/user/{user_id}")
def read_by_user(user_id: int, db: Session = Depends(get_db)):
    return get_notes_by_user(db, user_id)


@router.put("/{note_id}")
def update(note_id: int, data: NoteUpdate, db: Session = Depends(get_db)):
    return update_note(db, note_id, data.description)


@router.delete("/{note_id}")
def delete(note_id: int, db: Session = Depends(get_db)):
    return delete_note(db, note_id)