from pydantic import BaseModel, EmailStr,Field

class UserCreate(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    email: EmailStr 
    password: str = Field(..., min_length=6)
    contact_no: str = Field(..., min_length=10, max_length=10)


class UserUpdate(BaseModel):
    name: str
    contact_no: str
    is_active: bool