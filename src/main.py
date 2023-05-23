
from http.client import HTTPResponse
from re import template
from typing import Annotated, Union

from fastapi import FastAPI, Form, Request, UploadFile, Depends

from users.routers import user_router
from audio.routers import audio_router

app = FastAPI()

app.include_router(user_router)
app.include_router(audio_router)

# @app.post("/file/upload-file")
# def upload_file(file: UploadFile):
#   print(file)
#   return file


# @app.post("/login/")
# async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
#     return {"username": username}
