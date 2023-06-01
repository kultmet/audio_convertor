from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, Request, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.responses import FileResponse

from src.database import get_async_session

from src.audio.schemas import AudioID, AudioPath
from src.audio.utils import save, select_data, wav_to_mp3, check_authorization
from src.users.utils import content_type_validation

audio_router = APIRouter()


@audio_router.post(
    '/audio/',
    tags=['Audio']
)
async def converts_audio(
    request: Request,
    user_id: UUID,
    user_token: UUID,
    wav_file: UploadFile,
    db_session: AsyncSession = Depends(get_async_session)
):
    """
    For converts wav-audio file to mp3-audio file
    and returns url for downloading result file.
    """
    await content_type_validation(wav_file.content_type)
    await check_authorization(db_session, user_id, user_token)
    path = await wav_to_mp3(wav_file)
    await save(db_session, user_id, path)
    song_id = await select_data(db_session, user_id, path)
    return (
        f'{request.url_for("upload_file")}'
        f'?id={AudioID.from_orm(song_id).id}&user={user_id}'
    )


@audio_router.get(
    '/record',
    tags=['Audio'],
)
async def upload_file(
    id: UUID,
    user: UUID,
    db_session: AsyncSession = Depends(get_async_session)
):
    """Downloading mp3-audio file."""
    song_path = await select_data(
        db_session=db_session, user_id=user, song_id=id
    )
    return FileResponse(path=AudioPath.from_orm(song_path).path)
