from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.services.spotify_service import get_spotify_token, SPOTIFY_SEARCH_URL
from app.models.search_history_model import SearchHistory, SearchTypeEnum
from app.models.music_action_model import MusicAction, ActionEnum
from app.schemas.user import User
from app.utils.dependencies import get_db, get_user_or_404
import requests

router = APIRouter(prefix="/spotify", tags=["Spotify"])

@router.get("/search")
def search_spotify(query: str, user: User = Depends(get_user_or_404),  type: SearchTypeEnum = SearchTypeEnum.track, db: Session = Depends(get_db)):
    token = get_spotify_token()

    headers = {"Authorization": f"Bearer {token}"}
    params = {"q": query, "type": type, "limit": 10}

    response = requests.get(SPOTIFY_SEARCH_URL, headers=headers, params=params)
    if response.status_code != 200:
        raise HTTPException(500, "Spotify API error")

    db_search = SearchHistory(
        user_id=user.id,
        query=query,
        type=type,
    )
    db.add(db_search)
    db.commit()

    return response.json()

@router.post("/action")
def music_action(
    spotify_id: str,
    action: ActionEnum,
    user: User = Depends(get_user_or_404),
    type: SearchTypeEnum = SearchTypeEnum.track,
    db: Session = Depends(get_db)
):
    if isinstance(action, ActionEnum):
        raise HTTPException(400, "Action must be 'like' or 'dislike'")
    if isinstance(type, SearchTypeEnum):
        raise HTTPException(400, "Type must be 'track', 'album' or 'artist'")

    action = MusicAction(
        user_id=user.id,
        spotify_id=spotify_id,
        type=type,
        action=action
    )

    db.add(action)
    db.commit()
    db.refresh(action)

    return {"message": f"{action} saved", "data": action}
