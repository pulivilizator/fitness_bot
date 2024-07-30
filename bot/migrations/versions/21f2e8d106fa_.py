"""empty message

Revision ID: 21f2e8d106fa
Revises: 7b5b29ef30f5
Create Date: 2024-07-30 23:16:48.410141

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '21f2e8d106fa'
down_revision: Union[str, None] = '7b5b29ef30f5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_calories', sa.Column('maximum', sa.SmallInteger(), nullable=True))
    op.add_column('user_calories', sa.Column('current', sa.SmallInteger(), nullable=False))
    op.drop_column('user_calories', 'maximum_quantity')
    op.drop_column('user_calories', 'current_quantity')
    op.add_column('users', sa.Column('activity', sa.Enum('HIGH', 'MEDIUM', 'LOW', name='activelevel'), nullable=True))
    op.drop_column('users', 'activity_level')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('activity_level', postgresql.ENUM('HIGH', 'MEDIUM', 'LOW', name='activelevel'), autoincrement=False, nullable=True))
    op.drop_column('users', 'activity')
    op.add_column('user_calories', sa.Column('current_quantity', sa.SMALLINT(), autoincrement=False, nullable=False))
    op.add_column('user_calories', sa.Column('maximum_quantity', sa.SMALLINT(), autoincrement=False, nullable=True))
    op.drop_column('user_calories', 'current')
    op.drop_column('user_calories', 'maximum')
    # ### end Alembic commands ###