from pydantic import BaseModel

class SearchHistoryBase(BaseModel):
    query: str
    type: str

class SearchHistoryResponse(SearchHistoryBase):
    id: int

    class Config:
        orm_mode = True
