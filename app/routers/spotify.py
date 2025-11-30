from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.search_history_model import SearchTypeEnum
from app.models.music_action_model import ActionEnum
from app.schemas.user import User
from app.services.spotify_service import get_search, get_music_action
from app.utils.dependencies import get_db, get_user_or_404

router = APIRouter(prefix="/spotify", tags=["Spotify"])

@router.get("/search")
def search_spotify(query: str, user: User = Depends(get_user_or_404),  type: SearchTypeEnum = SearchTypeEnum.track, db: Session = Depends(get_db)):
    return get_search(query, user, type, db)

@router.post("/action")
def music_action(
    spotify_id: str,
    action: ActionEnum,
    user: User = Depends(get_user_or_404),
    type: SearchTypeEnum = SearchTypeEnum.track,
    db: Session = Depends(get_db)
):
    return get_music_action(user, action, spotify_id, type, db)
