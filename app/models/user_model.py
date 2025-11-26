from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    country = Column(String)

    searches = relationship("SearchHistory", back_populates="user")
    music_actions = relationship("MusicAction", back_populates="user")




