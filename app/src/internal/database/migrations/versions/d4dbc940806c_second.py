"""second

Revision ID: d4dbc940806c
Revises: 6519b6696c94
Create Date: 2023-08-12 05:56:44.686293

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "d4dbc940806c"
down_revision: Union[str, None] = "6519b6696c94"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("username", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=False),
        sa.Column("registered_at", sa.TIMESTAMP(), nullable=True),
        sa.Column("avatar", sa.String(), nullable=True),
        sa.Column("first_name", sa.String(), nullable=True),
        sa.Column("last_name", sa.String(), nullable=True),
        sa.Column("role", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["role"],
            ["role.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.drop_table("user")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "user",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("email", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column("username", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column("password", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column(
            "registered_at", postgresql.TIMESTAMP(), autoincrement=False, nullable=True
        ),
        sa.Column("avatar", sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column("first_name", sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column("last_name", sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column("role", sa.INTEGER(), autoincrement=False, nullable=True),
        sa.ForeignKeyConstraint(["role"], ["role.id"], name="user_role_fkey"),
        sa.PrimaryKeyConstraint("id", name="user_pkey"),
    )
    op.drop_table("users")
    # ### end Alembic commands ###
