from app.models.user_model import User
from app.models.user_preference_model import UserPreference
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate
from app.schemas.user_preference import UserPreferenceCreate

def get_users(db: Session):
    return db.query(User).all()

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

# Preferences
def create_preference(db: Session, pref: UserPreferenceCreate, user_id: int):
    db_pref = UserPreference(**pref.dict(), user_id=user_id)
    db.add(db_pref)
    db.commit()
    db.refresh(db_pref)
    return db_pref
