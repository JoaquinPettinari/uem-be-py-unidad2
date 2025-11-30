from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.user_model import User

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_user_or_404(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(404, "User not found")
    return user
