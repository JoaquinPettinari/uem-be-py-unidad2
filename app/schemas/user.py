from pydantic import BaseModel
from .music_action import MusicActionResponse
from .search_history import SearchHistoryResponse

class UserBase(BaseModel):
    name: str
    age: int
    country: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    searches: list[SearchHistoryResponse] = []
    music_actions: list[MusicActionResponse] = []

    model_config = {"from_attributes": True}
