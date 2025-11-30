from pydantic import BaseModel
from enum import Enum

class SearchTypeEnum(str, Enum):
    track = "track"
    artist = "artist"
    album = "album"

class SearchHistoryBase(BaseModel):
    query: str
    type: SearchTypeEnum

class SearchHistoryResponse(SearchHistoryBase):
    id: int

    model_config = {"from_attributes": True}
