from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.user_models import Base

class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String(255))
    user_id = Column(Integer, ForeignKey("users.id"))

    # Relationship
    user = relationship("User", backref="notes")