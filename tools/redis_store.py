# Auto-generated
import redis
from utils.config import get_settings

settings = get_settings()

r = redis.Redis(host=settings.redis_host, port=settings.redis_port)


def increment_request(user_id: str):
    key = f"user:{user_id}:requests"
    return r.incr(key)


def check_velocity(user_id: str):
    count = increment_request(user_id)
    return count > 5