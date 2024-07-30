"""empty message

Revision ID: 59f808a69e3a
Revises: 
Create Date: 2024-07-22 22:48:36.194030

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '59f808a69e3a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('telegram_id', sa.BigInteger(), nullable=False),
    sa.Column('activity_level', sa.Enum('HIGH', 'MEDIUM', 'LOW', name='activelevel'), nullable=True),
    sa.Column('gender', sa.Enum('MALE', 'FEMALE', name='sex'), nullable=True),
    sa.Column('weight', sa.SmallInteger(), nullable=True),
    sa.Column('height', sa.SmallInteger(), nullable=True),
    sa.Column('age', sa.SmallInteger(), nullable=True),
    sa.Column('status', sa.Enum('NEW', 'USER', 'ADMIN', name='userstatus'), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('last_updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('telegram_id')
    )
    op.create_table('user_calories',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('maximum_quantity', sa.SmallInteger(), nullable=True),
    sa.Column('current_quantity', sa.SmallInteger(), nullable=False),
    sa.Column('last_updated_at', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.BigInteger(), nullable=False),
    sa.CheckConstraint('current_quantity >=0', name='current_quantity_check'),
    sa.ForeignKeyConstraint(['user_id'], ['users.telegram_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_settings',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('language', sa.Enum('RU', 'EN', name='language'), nullable=False),
    sa.Column('automatic_calorie_counting', sa.Boolean(), nullable=False),
    sa.Column('timezone', sa.String(length=7), nullable=False),
    sa.Column('last_updated_at', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.BigInteger(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.telegram_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_settings')
    op.drop_table('user_calories')
    op.drop_table('users')
    # ### end Alembic commands ###