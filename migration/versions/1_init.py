"""init

Revision ID: 1d13e41cac94
Revises: 
Create Date: 2023-05-21 20:01:16.864459

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('token', sa.UUID(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=True)
    op.create_index(op.f('ix_users_token'), 'users', ['token'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('audio',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('user', sa.UUID(), nullable=False),
    sa.Column('path', sa.String(), nullable=False),
    sa.Column('date_added', sa.TIMESTAMP(), nullable=False),
    sa.ForeignKeyConstraint(['user'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_audio_id'), 'audio', ['id'], unique=False)
    op.create_index(op.f('ix_audio_user'), 'audio', ['user'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_audio_user'), table_name='audio')
    op.drop_index(op.f('ix_audio_id'), table_name='audio')
    op.drop_table('audio')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_token'), table_name='users')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
