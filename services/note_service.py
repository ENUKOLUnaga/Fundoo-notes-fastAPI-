from models.note_model import Note
from models.user_models import User
from fastapi import HTTPException
from utils.loggers import logger


# CREATE NOTE
def create_note(db, note):
    user = db.query(User).filter(User.id == note.user_id).first()

    if not user:
        logger.warning(f"User {note.user_id} not found")
        raise HTTPException(status_code=404, detail="User not found")

    new_note = Note(
        description=note.description,
        user_id=note.user_id
    )

    db.add(new_note)
    db.commit()
    db.refresh(new_note)

    logger.info(f"Note created for user {note.user_id}")
    return new_note


# GET ALL NOTES
def get_notes(db):
    notes = db.query(Note).all()
    logger.info(f"{len(notes)} notes fetched")
    return notes


# GET NOTES BY USER
def get_notes_by_user(db, user_id):
    notes = db.query(Note).filter(Note.user_id == user_id).all()

    logger.info(f"{len(notes)} notes fetched for user {user_id}")
    return notes


# UPDATE NOTE
def update_note(db, note_id, description):
    note = db.query(Note).filter(Note.id == note_id).first()

    if not note:
        logger.warning(f"Note {note_id} not found")
        raise HTTPException(status_code=404, detail="Note not found")

    note.description = description
    db.commit()
    db.refresh(note)

    logger.info(f"Note {note_id} updated")
    return note


# DELETE NOTE
def delete_note(db, note_id):
    note = db.query(Note).filter(Note.id == note_id).first()

    if not note:
        logger.warning(f"Note {note_id} not found")
        raise HTTPException(status_code=404, detail="Note not found")

    db.delete(note)
    db.commit()

    logger.info(f"Note {note_id} deleted")
    return {"message": "Note deleted"}