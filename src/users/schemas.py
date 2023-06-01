from uuid import UUID

from pydantic import BaseModel


class ResponseUser(BaseModel):
    id: UUID
    token: UUID

    class Config:
        orm_mode = True
