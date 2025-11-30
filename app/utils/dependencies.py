from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.services.user_service import get_user

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_user_or_404(user_id: int, db: Session = Depends(get_db)):
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(404, "User not found")
    return user
