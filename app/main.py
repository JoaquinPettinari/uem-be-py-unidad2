from fastapi import FastAPI
from .database import Base, engine
from .routers import users, spotify
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(spotify.router)
