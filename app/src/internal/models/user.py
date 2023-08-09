from pydantic import BaseModel


class BaseUser(BaseModel):
    email: str
    password: str
    firstname: str
    lastname: str
