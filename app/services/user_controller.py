from app.models.user_model import User
from sqlalchemy.orm import Session, joinedload
from app.schemas.user import UserCreate

def get_users(db: Session):
    return db.query(User)\
        .options(joinedload(User.searches), joinedload(User.music_actions))\
        .all()

def create_user(db: Session, user: UserCreate):
    db_user = User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def delete_user(db: Session, user_id: int):
    user = get_user(db, user_id)
    if user:
        db.delete(user)
        db.commit()
    return user
