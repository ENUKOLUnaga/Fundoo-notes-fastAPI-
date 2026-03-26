from pydantic import BaseModel, Field


class NoteCreate(BaseModel):
    description: str = Field(..., min_length=3)
    user_id: int


class NoteUpdate(BaseModel):
    description: str = Field(..., min_length=3)