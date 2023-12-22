from datetime import datetime

from sqlalchemy import (
    MetaData,
    Table,
    Column,
    String,
    Integer,
    TIMESTAMP,
    Boolean,
    ForeignKey,
    JSON,
)
from sqlalchemy.orm import (
    declarative_base,
)


Base = declarative_base()


class Role(Base):
    __tablename__ = "role"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    status = Column(String, nullable=False)
    permissions = Column(JSON)


class User(Base):
    __tablename__ = "user"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow())
    avatar = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    role = Column(Integer, ForeignKey("role.id"))
    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(Boolean, default=True, nullable=False)
    is_verified = Column(Boolean, default=True, nullable=False)
