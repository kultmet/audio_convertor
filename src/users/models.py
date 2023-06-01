from uuid import uuid4
from sqlalchemy import UUID, Column, MetaData, String, Table

metadata: MetaData = MetaData()


user: Table = Table(
    'users',
    metadata,
    Column(
        'id',
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
        index=True
    ),
    Column('username', String(), index=True, nullable=False),
    Column(
        'token',
        UUID(as_uuid=True),
        unique=True,
        index=True,
        default=uuid4,
        nullable=False
    )
)
