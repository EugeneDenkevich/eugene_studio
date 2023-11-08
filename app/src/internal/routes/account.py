from fastapi import APIRouter, Depends

from app.src.internal.database.auth.manager import fastapi_users
from app.src.internal.database.models import User


current_user = fastapi_users.current_user()

routes = APIRouter(
    prefix="",
    tags=["account"]
)


@routes.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.username}"
