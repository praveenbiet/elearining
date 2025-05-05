from typing import Optional

import redis
from redis import Redis

from .config import get_settings

settings = get_settings()

# Create Redis connection pool
redis_pool = redis.ConnectionPool(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    password=settings.REDIS_PASSWORD,
    db=settings.REDIS_DB,
    decode_responses=True,
)


def get_redis() -> Redis:
    """Get Redis client."""
    return redis.Redis(connection_pool=redis_pool)


def get_cached_value(key: str) -> Optional[str]:
    """Get value from Redis cache."""
    redis_client = get_redis()
    return redis_client.get(key)


def set_cached_value(key: str, value: str, expire: int = 3600) -> bool:
    """Set value in Redis cache."""
    redis_client = get_redis()
    return redis_client.set(key, value, ex=expire)


def delete_cached_value(key: str) -> bool:
    """Delete value from Redis cache."""
    redis_client = get_redis()
    return redis_client.delete(key) > 0 