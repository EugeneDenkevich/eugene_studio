from fastapi import FastAPI
from dataclasses import dataclass


@dataclass(frozen=True)
class Routes:

    routes: tuple

    def register_routes(self, app: FastAPI):
        for route in self.routes:
            app.include_router(route)
