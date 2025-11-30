from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, User
from ..database import SessionLocal
from app.services.user_controller import create_user, delete_user, get_user, get_users
from app.utils.dependencies import get_db
router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/", response_model=list[User])
def get_users_route(db: Session = Depends(get_db)):
    return get_users(db)

@router.post("/", response_model=User)
def create_user_route(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@router.get("/{user_id}", response_model=User)
def read_user_route(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id)
    if not db_user:
        raise HTTPException(404, "User not found")
    return db_user

@router.delete("/{user_id}", response_model=User)
def delete_user_route(user_id: int, db: Session = Depends(get_db)):
    deleted = delete_user(db, user_id)
    if not deleted:
        raise HTTPException(404, "User not found")
    return deleted
