from app.src.config.routes import routes
from app.src.internal.routes import account


__routes__ = routes.Routes(routes=(account.routes, ))
