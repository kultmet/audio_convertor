from fastapi import HTTPException
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError


from src.users.models import user


async def save_user(db_session: AsyncSession, username: str):
    try:
        await db_session.execute(insert(user).values(username=username))
        await db_session.commit()
    except IntegrityError:
        raise HTTPException(
            403, f'Пользователь с именем {username} уже существует.'
        )


async def get_user(db_session: AsyncSession, username: str):
    query = select(user).where(user.c.username == username)
    return await db_session.execute(query)


async def content_type_validation(content_type):
    if content_type != 'audio/wav':
        raise HTTPException(
            400, 'Invalid content type. Можно только файлы в расширением wav!'
        )
