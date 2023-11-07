"""new user table

Revision ID: 4e1932f3be33
Revises: 01671997a8d9
Create Date: 2023-08-12 11:00:37.491575

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '4e1932f3be33'
down_revision: Union[str, None] = '01671997a8d9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.Column('registered_at', sa.TIMESTAMP(), nullable=True),
    sa.Column('avatar', sa.String(), nullable=True),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('role', sa.Integer(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('is_superuser', sa.Boolean(), nullable=False),
    sa.Column('is_verified', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['role'], ['role.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_constraint('role_role_fkey', 'role', type_='foreignkey')
    op.drop_column('role', 'username')
    op.drop_column('role', 'registered_at')
    op.drop_column('role', 'first_name')
    op.drop_column('role', 'last_name')
    op.drop_column('role', 'email')
    op.drop_column('role', 'password')
    op.drop_column('role', 'role')
    op.drop_column('role', 'avatar')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('role', sa.Column('avatar', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('role', sa.Column('role', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('role', sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('role', sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('role', sa.Column('last_name', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('role', sa.Column('first_name', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('role', sa.Column('registered_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column('role', sa.Column('username', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.create_foreign_key('role_role_fkey', 'role', 'role', ['role'], ['id'])
    op.drop_table('user')
    # ### end Alembic commands ###