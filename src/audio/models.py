from datetime import datetime

from uuid import uuid4
from sqlalchemy import (
    UUID, Column, ForeignKey, MetaData, String, Table, TIMESTAMP
)

from src.users.models import user

metadata: MetaData = MetaData()


audio: Table = Table(
    'audio',
    metadata,
    Column(
        'id', UUID(as_uuid=True), primary_key=True, default=uuid4, index=True
    ),
    Column('user', ForeignKey(user.c.id), index=True, nullable=False),
    Column('path', String, nullable=False),
    Column('date_added', TIMESTAMP, default=datetime.utcnow, nullable=False),
)
