import redis.asyncio
from fastapi_users.authentication import (
    RedisStrategy,
    AuthenticationBackend,
    BearerTransport,
)


bearer_transport = BearerTransport(tokenUrl="auth/bearer/login")

redis = redis.asyncio.from_url("redis://redis:6379", decode_responses=True)


def get_redis_strategy() -> RedisStrategy:
    return RedisStrategy(redis, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="redis",
    transport=bearer_transport,
    get_strategy=get_redis_strategy,
)
