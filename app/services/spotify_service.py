import base64
import os
import requests
from sqlalchemy.orm import Session
from fastapi import HTTPException
from dotenv import load_dotenv
from app.models.search_history_model import SearchHistory, SearchTypeEnum
from app.schemas.user import User
from app.models.music_action_model import MusicAction, ActionEnum

load_dotenv()

SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"
SPOTIFY_SEARCH_URL = "https://api.spotify.com/v1/search"

def get_search(query: str, user: User, type: SearchTypeEnum, db: Session):
    spotify_search = get_spotify_search(query, type)
    db_search = SearchHistory(
        user_id=user.id,
        query=query,
        type=type,
    )
    db.add(db_search)
    db.commit()
    db.refresh(db_search)

    return spotify_search

def get_searches_by_user_id(user: User, db: Session):
    return db.query(SearchHistory).filter(SearchHistory.user_id == user.id).all()

def get_actions_by_user_id(user: User, db: Session):
    return db.query(MusicAction).filter(MusicAction.user_id == user.id).all()

def get_music_action(user: User, action: ActionEnum, spotify_id: str, type: SearchTypeEnum, db: Session ):
    if not isinstance(action, ActionEnum):
        raise HTTPException(400, "Action must be 'like' or 'dislike'")
    if not isinstance(type, SearchTypeEnum):
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

def delete_music_action(db: Session, action_id: int):
    action = db.query(MusicAction).filter(MusicAction.id == action_id).first()
    if not action:
        raise HTTPException(404, "Action not found")

    db.delete(action)
    db.commit()

    return action

def get_spotify_token():
    client_id = os.getenv("SPOTIFY_CLIENT_ID")
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

    if not client_id or not client_secret:
        raise HTTPException(500, "Spotify credentials are missing in environment variables")

    auth_string = f"{client_id}:{client_secret}"
    auth_base64 = base64.b64encode(auth_string.encode()).decode()

    headers = {
        "Authorization": f"Basic {auth_base64}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}

    response = requests.post(SPOTIFY_TOKEN_URL, headers=headers, data=data)
    response.raise_for_status()

    token = response.json().get("access_token")
    return token

def get_spotify_search(query: str, type: SearchTypeEnum):
    token = get_spotify_token()

    headers = {"Authorization": f"Bearer {token}"}
    params = {"q": query, "type": type, "limit": 10}

    request = requests.get(SPOTIFY_SEARCH_URL, headers=headers, params=params)

    if request.status_code != 200:
        raise HTTPException(500, "Spotify API error")

    return request.json()
