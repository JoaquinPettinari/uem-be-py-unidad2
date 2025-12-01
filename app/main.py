from fastapi import FastAPI
from .database import Base, engine
from .routers import users, spotify
from dotenv import load_dotenv
from app.database import SessionLocal
from app.seed import run_seed

load_dotenv()

app = FastAPI()

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(spotify.router)

@app.on_event("startup")
def startup_event():
    db = SessionLocal()
    try:
        run_seed(db)
    finally:
        db.close()
