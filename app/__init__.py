from fastapi import FastAPI

from app.src.internal.database.auth.schemas import UserCreate, UserRead

from .src.config.server import Server
from app.src.internal.database.auth.backend import auth_backend
from app.src.internal.database.auth.manager import fastapi_users


tags = [
    {
        "name": "account",
        "description": "Operations with user's account"
    },
    {
        "name": "auth",
        "description": "Operations with users by fastapi-users"
    },
]


def create_app(_=None) -> FastAPI:
    """
    The app's entrypoint
    """
    # Create the FastAPI instance
    app = FastAPI(
        title="Eugene Studio. Blog",
        docs_url="/swagger",
        version='0.02',
        openapi_tags=tags
    )

    # Register fastap-users routers
    routers = (
        fastapi_users.get_auth_router(auth_backend),
        fastapi_users.get_register_router(UserRead, UserCreate),
    )
    include_fastapiusers_routers(app=app, routers=routers)
    
    return Server(app).get_app()


def include_fastapiusers_routers(app: FastAPI, routers: tuple):
    for router in routers:
        app.include_router(
            router=router,
            prefix="/auth/bearer",
            tags=["auth"]
        )