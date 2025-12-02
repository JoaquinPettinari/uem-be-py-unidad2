from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from app.models.user_model import User
from app.models.search_history_model import SearchHistory, SearchTypeEnum
from app.models.music_action_model import MusicAction, ActionEnum
from app.utils.dependencies import get_db

def run_seed(db: Session):
    try:
        print('------------------------')
        if db.query(User).count() > 0:
            print("Seed already executed.")
            return

        user_list = [
            User(name="Joaquín", age=27, country="Argentina"),
            User(name="Marcelo", age=15, country="Brasil"),
            User(name="Julian", age=23, country="Italy")
        ]
        db.add_all(user_list)
        db.commit()

        search = SearchHistory(
            user_id=user_list[0].id,
            query="Metallica",
            type=SearchTypeEnum.artist
        )
        db.add(search)

        action = MusicAction(
            user_id=user_list[0].id,
            spotify_id="55tK4Ab7XHTOKkw0xDz3AA",
            type=SearchTypeEnum.track,
            action=ActionEnum.like
        )
        db.add(action)

        db.commit()

        print("Seed executed successfully!")

    except SQLAlchemyError:
        db.rollback()
        raise

