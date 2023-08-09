from fastapi import FastAPI

from .src.config.server import Server


tags = [
    {
        "name": "Users",
        "description": "Operations with users"
    },
]

def create_app(_=None) -> FastAPI:
    app = FastAPI(
        docs_url="/swagger",
        openapi_tags=tags
    )
    return Server(app).get_app()