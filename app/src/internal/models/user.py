from pydantic import BaseModel, Field


class BaseUser(BaseModel):
    id: int = Field(ge=1)
    email: str
    password: str
    firstname: str = Field(max_length=100)
    lastname: str = Field(max_length=100)
    age: int = Field(ge=0, le=100)
