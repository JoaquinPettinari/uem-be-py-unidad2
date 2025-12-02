from contextlib import asynccontextmanager
from fastapi import FastAPI
from dotenv import load_dotenv

from app.database import Base, engine, SessionLocal
from app.routers import users, spotify
from app.seed import run_seed

load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    db = SessionLocal()
    try:
        run_seed(db)
        yield
    finally:
        db.close()

app = FastAPI(lifespan=lifespan)

Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(spotify.router)
