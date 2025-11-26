from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

class MusicAction(Base):
    __tablename__ = "music_actions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    spotify_id = Column(String, index=True)
    type = Column(String)
    status = Column(String)

    user = relationship("User", back_populates="music_actions")
