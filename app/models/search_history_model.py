from sqlalchemy import Column, Integer, String, ForeignKey, Enum as SQLEnum
from sqlalchemy.orm import relationship
from ..database import Base
from app.schemas.search_history import SearchTypeEnum

class SearchHistory(Base):
    __tablename__ = "search_history"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    query = Column(String, index=True)
    type = Column(SQLEnum(SearchTypeEnum))

    user = relationship("User", back_populates="searches")
