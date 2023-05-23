from uuid import uuid4
from sqlalchemy import URL, UUID, Column, ForeignKey, MetaData, String, Table

from users.models import user

metadata: MetaData = MetaData()

def generate_url():
    return '/record?id=0&user=0'

audio: Table = Table(
    'audio',
    metadata,
    Column('id', UUID(as_uuid=True), primary_key=True, default=uuid4, index=True),
    Column('user', ForeignKey(user.c.id), index=True, nullable=False),
    Column('url', String, index=True, default=generate_url, nullable=False)
)