from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_async_session

from src.users.models import user

from src.users.schemas import ResponseUser

user_router = APIRouter()


@user_router.post(
    path='/users/',
    tags=['Users'],
    response_model=ResponseUser
)
async def create_user(
    username: str, session: AsyncSession = Depends(get_async_session)
):
    """Create user API View."""
    await session.execute(insert(user).values(username=username))
    await session.commit()
    query = select(user)
    result = await session.execute(query)
    return ResponseUser.from_orm(result.first())


@user_router.get(
    '/users/',
    tags=['Users'],
    response_model=List[ResponseUser]
)
async def all_users(db_session: AsyncSession = Depends(get_async_session)):
    """Get all users API View."""
    query = select(user)
    result = await db_session.execute(query)
    return [ResponseUser.from_orm(obj) for obj in result.all()]
