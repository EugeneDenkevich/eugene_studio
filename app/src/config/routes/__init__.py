from app.src.config.routes import routes
from app.src.internal.routes import users


__routes__ = routes.Routes(routes=(users.routes,))