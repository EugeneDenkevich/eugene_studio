"""thrid

Revision ID: 01671997a8d9
Revises: d4dbc940806c
Create Date: 2023-08-12 06:14:41.124423

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '01671997a8d9'
down_revision: Union[str, None] = 'd4dbc940806c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.add_column('role', sa.Column('email', sa.String(), nullable=False))
    op.add_column('role', sa.Column('username', sa.String(), nullable=False))
    op.add_column('role', sa.Column('password', sa.String(), nullable=False))
    op.add_column('role', sa.Column('registered_at', sa.TIMESTAMP(), nullable=True))
    op.add_column('role', sa.Column('avatar', sa.String(), nullable=True))
    op.add_column('role', sa.Column('first_name', sa.String(), nullable=True))
    op.add_column('role', sa.Column('last_name', sa.String(), nullable=True))
    op.add_column('role', sa.Column('role', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'role', 'role', ['role'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'role', type_='foreignkey')
    op.drop_column('role', 'role')
    op.drop_column('role', 'last_name')
    op.drop_column('role', 'first_name')
    op.drop_column('role', 'avatar')
    op.drop_column('role', 'registered_at')
    op.drop_column('role', 'password')
    op.drop_column('role', 'username')
    op.drop_column('role', 'email')
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('username', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('registered_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('avatar', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('first_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('last_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('role', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['role'], ['role.id'], name='users_role_fkey'),
    sa.PrimaryKeyConstraint('id', name='users_pkey')
    )
    # ### end Alembic commands ###
