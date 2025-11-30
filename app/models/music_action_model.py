from sqlalchemy import Column, Integer, String, ForeignKey, Enum as SQLEnum
from app.schemas.music_action import ActionEnum
from app.schemas.search_history import SearchTypeEnum
from sqlalchemy.orm import relationship
from ..database import Base

class MusicAction(Base):
    __tablename__ = "music_actions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    spotify_id = Column(String, index=True)
    type = Column(SQLEnum(SearchTypeEnum))
    action = Column(SQLEnum(ActionEnum))

    user = relationship("User", back_populates="music_actions")
