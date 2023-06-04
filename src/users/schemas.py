from uuid import UUID

from pydantic import BaseModel


class RequestUsername(BaseModel):
    username: str


class ResponseUser(BaseModel):
    id: UUID
    token: UUID

    class Config:
        orm_mode = True
