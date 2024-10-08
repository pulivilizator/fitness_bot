"""empty message

Revision ID: 7b5b29ef30f5
Revises: 59f808a69e3a
Create Date: 2024-07-25 22:09:50.966517

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7b5b29ef30f5'
down_revision: Union[str, None] = '59f808a69e3a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('user_calories_user_id_fkey', 'user_calories', type_='foreignkey')
    op.create_foreign_key(None, 'user_calories', 'users', ['user_id'], ['telegram_id'], ondelete='CASCADE')
    op.drop_constraint('user_settings_user_id_fkey', 'user_settings', type_='foreignkey')
    op.create_foreign_key(None, 'user_settings', 'users', ['user_id'], ['telegram_id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user_settings', type_='foreignkey')
    op.create_foreign_key('user_settings_user_id_fkey', 'user_settings', 'users', ['user_id'], ['telegram_id'])
    op.drop_constraint(None, 'user_calories', type_='foreignkey')
    op.create_foreign_key('user_calories_user_id_fkey', 'user_calories', 'users', ['user_id'], ['telegram_id'])
    # ### end Alembic commands ###
