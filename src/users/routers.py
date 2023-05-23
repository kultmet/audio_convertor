from fastapi import APIRouter, Depends
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session

from users.models import user

from users.schemas import ResponseUser

user_router = APIRouter()


@user_router.post(
    path='/users/',
    tags=['Users'],
    response_model=ResponseUser
)
async def create_user(username: str, session: AsyncSession = Depends(get_async_session)):
    
    await session.execute(insert(user).values(username=username))
    await session.commit()
    query = select(user)
    result = await session.execute(query)
    return ResponseUser.from_orm(result.first())
