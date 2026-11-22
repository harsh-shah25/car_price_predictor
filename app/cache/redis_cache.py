import json
import redis
from app.core.config import settings


redis_client = redis.StrictRedis.from_url(settings.REDIS_URL, decode_responses=True)


def get_cached_prediction(key: str):
    value = redis_client.get(key)

    if value:
        return json.loads(value)

    return None


def set_cached_prediction(key: str, value: dict, expiry: int = 3600):
    redis_client.setex(key, expiry, json.dumps(value))