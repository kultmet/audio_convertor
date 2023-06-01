from fastapi import FastAPI

from src.users.routers import user_router
from src.audio.routers import audio_router

app = FastAPI()

app.include_router(user_router)
app.include_router(audio_router)
