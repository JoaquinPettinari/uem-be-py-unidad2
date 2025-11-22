from pydantic import BaseModel
from typing import List
from .user_preference import UserPreference  # <-- schema, no modelo ORM

class UserBase(BaseModel):
    name: str
    age: int
    country: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    preferences: List[UserPreference] = []

    model_config = {"from_attributes": True}
