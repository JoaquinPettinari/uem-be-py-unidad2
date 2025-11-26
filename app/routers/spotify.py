from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from app.services.spotify_service import get_spotify_token, SPOTIFY_SEARCH_URL
from app.models.search_history_model import SearchHistory
from app.models.music_action_model import MusicAction
import requests

router = APIRouter(prefix="/spotify", tags=["Spotify"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/search")
def search_spotify(user_id: int, query: str, type: str = "track", db: Session = Depends(get_db)):
    token = get_spotify_token()

    headers = {"Authorization": f"Bearer {token}"}
    params = {"q": query, "type": type, "limit": 10}

    response = requests.get(SPOTIFY_SEARCH_URL, headers=headers, params=params)
    if response.status_code != 200:
        raise HTTPException(500, "Spotify API error")

    db_search = SearchHistory(
        user_id=user_id,
        query=query,
        type=type,
    )
    db.add(db_search)
    db.commit()

    return response.json()

@router.post("/action")
def music_action(
    user_id: int,
    spotify_id: str,
    type: str,
    status: str,
    db: Session = Depends(get_db)
):
    if status not in ["like", "dislike"]:
        raise HTTPException(400, "Status must be 'like' or 'dislike'")

    action = MusicAction(
        user_id=user_id,
        spotify_id=spotify_id,
        type=type,
        status=status
    )

    db.add(action)
    db.commit()
    db.refresh(action)

    return {"message": f"{status} saved", "data": action}
