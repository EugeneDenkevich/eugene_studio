from datetime import datetime

from sqlalchemy import (
    MetaData, Table, Column, String, Integer, TIMESTAMP,
    ForeignKey, JSON)
from sqlalchemy.orm import (declarative_base, DeclarativeBase)


Base = declarative_base()


class Role(Base):
    __tablename__ = "role"
    __table_args__ = {'extend_existing': True} 

    id = Column(Integer, primary_key=True)
    status = Column(String, nullable=False)
    permissions = Column(JSON)


class Users(Base):
    __tablename__ = "role"
    __table_args__ = {'extend_existing': True} 

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow())
    avatar = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    role = Column(Integer, ForeignKey("role.id"))
