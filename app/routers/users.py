from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, User
from app.services.user_service import create_user, delete_user, get_users
from app.utils.dependencies import get_db, get_user_or_404

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/", response_model=list[User])
def get_users_route(db: Session = Depends(get_db)):
    return get_users(db)

@router.post("/", response_model=User)
def create_user_route(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@router.get("/{user_id}", response_model=User)
def read_user_route(user: int = Depends(get_user_or_404)):
    return user

@router.delete("/{user_id}", response_model=User)
def delete_user_route(user_id: int, db: Session = Depends(get_db)):
    deleted = delete_user(db, user_id)
    if not deleted:
        raise HTTPException(404, "User not found")
    return deleted
