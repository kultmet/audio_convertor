from typing import Annotated
from uuid import UUID
from fastapi import APIRouter, Depends, Form, UploadFile
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session

from audio.models import audio
from audio.schemas import AudioRequest
from audio.utils import wav_to_mp3

audio_router = APIRouter()

@audio_router.post(
    '/audio/',
    tags=['Audio']
    # response_model=UploadFile
)
async def converts_audio(
    user_id: Annotated[UUID, Form()],
    user_token: Annotated[UUID, Form()],
    wav_file: UploadFile
):
    wav_to_mp3(wav_file)
    return 'fuck'# Нужно сформировать ссылу на эндпоинт следующей функции или как то по другому решить этот вопрос


@audio_router.get(
    '/audio/',
    tags=['Audio'],
)
async def upload_file():
    pass