# Auto-generated
import logging
import json
import time

def get_logger(name: str):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger

logger = get_logger("app")


def trace_node(func):
    async def wrapper(*args, **kwargs):
        start = time.time()
        result = await func(*args, **kwargs)
        duration = round(time.time() - start, 3)

        logger.info(json.dumps({
            "node": func.__name__,
            "duration": duration
        }))
        return result
    return wrapper