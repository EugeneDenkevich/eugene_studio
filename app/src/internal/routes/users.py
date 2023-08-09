from fastapi import APIRouter

from app.src.internal.models.user import BaseUser


routes = APIRouter(
    prefix="/api",
    tags=["Users"]
)


@routes.get("/users")
def get_user():
    """
    Get all users
    """
    return


@routes.get("/users/{id}")
def get_user(id: int):
    """
    Get a user by his id
    """
    return


@routes.post("/users")
def create_user(user: BaseUser):
    """
    Create a new user
    """
    return


@routes.put("/users/{id}")
def change_user(id: int):
    """
    Change an existing user
    """
    return


@routes.delete("/users/{id}")
def delete_user(id: int):
    """
    Delete a user by id
    """
    return