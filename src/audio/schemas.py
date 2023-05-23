from typing import Annotated
from uuid import UUID
from fastapi import Form, UploadFile
from pydantic import BaseModel, Field


class AudioRequest(BaseModel):
    user_id: Annotated[str, Form()]
    user_token: Annotated[str, Form()]

