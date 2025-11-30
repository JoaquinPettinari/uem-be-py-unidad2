from pydantic import BaseModel
from enum import Enum

class ActionEnum(str, Enum):
    like = "like"
    dislike = "dislike"

class MusicActionBase(BaseModel):
    spotify_id: str
    type: str
    action: ActionEnum

class MusicActionResponse(MusicActionBase):
    id: int

    model_config = {"from_attributes": True}
