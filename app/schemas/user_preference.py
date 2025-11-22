from pydantic import BaseModel

class UserPreferenceBase(BaseModel):
    favorite_genre: str
    favorite_artist: str

class UserPreferenceCreate(UserPreferenceBase):
    pass

class UserPreference(UserPreferenceBase):
    id: int
    user_id: int | None = None

    model_config = {"from_attributes": True}
