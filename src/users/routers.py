from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_async_session

from src.users.models import user

from src.users.schemas import ResponseUser, RequestUsername
from src.users.utils import get_user, save_user

user_router = APIRouter()


@user_router.post(
    path='/users/',
    tags=['Users'],
    response_model=ResponseUser,
    status_code=201,
)
async def create_user(
    username: RequestUsername,
    session: AsyncSession = Depends(get_async_session)
):
    """Create user API View. Returns id and token for created user."""
    await save_user(session, username.dict()['username'])
    result = await get_user(session, username.dict()['username'])
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
