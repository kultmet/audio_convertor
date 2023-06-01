import os
from pathlib import Path
from uuid import UUID

from fastapi import HTTPException, UploadFile
from pydub import AudioSegment
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.audio.models import audio
from src.constants import MEDIA_ROOT
from src.config import FFMPEG_PATH
from src.users.models import user


async def wav_to_mp3(wav_file: UploadFile) -> Path:
    """
    Saves WAV audio file, next Converts
    to MP3 audio and next remove WAV audio file.
    """
    filepath = f'{MEDIA_ROOT}/{wav_file.filename}'
    filename, _ = os.path.splitext(wav_file.filename)
    mp3_path = f'{MEDIA_ROOT}/{filename}.mp3'

    with open(filepath, 'wb') as file:
        file.write(wav_file.file.read())
    AudioSegment.converter = FFMPEG_PATH
    song = AudioSegment.from_wav(filepath)
    song.export(mp3_path, format='mp3')
    print(mp3_path)
    os.remove(filepath)
    return Path(mp3_path)


async def select_data(
        db_session: AsyncSession,
        user_id: UUID,
        path: Path | None = None,
        song_id: UUID | None = None
):
    if path:
        query = select(audio.c.id).where(
            audio.c.user == user_id, audio.c.path == str(path)
        ).order_by(audio.c.date_added)
    elif song_id:
        query = select(audio.c.path).where(
            audio.c.user == user_id, audio.c.id == str(song_id)
        ).order_by(audio.c.date_added)
    data = await db_session.execute(
        query
    )
    return data.first()


async def save(db_session: AsyncSession, user_id: UUID, path: Path):
    await db_session.execute(
        insert(audio).values(user=user_id, path=str(path))
    )
    await db_session.commit()


async def check_authorization(
        db_session: AsyncSession,
        user_id: UUID,
        user_token: UUID
):
    db_obj = await db_session.execute(
        select(user).where(user.c.id == user_id, user.c.token == user_token)
    )
    if not db_obj.scalar():
        raise HTTPException(401, 'Пользователя не существует')
