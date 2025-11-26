from pydantic import BaseModel

class MusicActionBase(BaseModel):
    spotify_id: str
    type: str
    status: str

class MusicActionResponse(MusicActionBase):
    id: int

    class Config:
        orm_mode = True
