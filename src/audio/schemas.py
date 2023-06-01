from typing import Annotated
from uuid import UUID

from fastapi import Form
from pydantic import BaseModel


class AudioRequest(BaseModel):
    user_id: Annotated[str, Form()]
    user_token: Annotated[str, Form()]


class AudioID(BaseModel):
    id: UUID

    class Config:
        orm_mode = True


class AudioPath(BaseModel):
    path: str

    class Config:
        orm_mode = True
