#!/usr/bin/env python3
"""Writing strings to Redis"""
from functools import wraps
from redis.client import Redis
from typing import Union, Callable, Optional, Any
import uuid


def count_calls(method: Callable) -> Callable:
    """Incrementing values"""
    data = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """wrapper func"""
        self._redis.incr(data)
        return method(self, *args, **kwds)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Storing lists"""
    data = method.__qualname__
    inputs = data + ":inputs"
    outputs = data + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """wrapper func"""
        self._redis.rpush(inputs, str(args))
        res = method(self, *args, **kwds)
        self._redis.rpush(outputs, str(res))
        return res
    return wrapper


def replay(method: Callable):
    """Retrieving lists"""
    data = method.__qualname__
    inputs = data + ":inputs"
    outputs = data + ":outputs"
    redis = method.__self__._redis
    count = redis.get(data).decode("utf-8")
    print(f"{data} was called {count} times:")
    in_list = redis.lrange(inputs, 0, -1)
    out_list = redis.lrange(outputs, 0, -1)
    redis_zipped = list(zip(in_list, out_list))
    for a, b in redis_zipped:
        attr, res = a.decode("utf-8"), b.decode("utf-8")
        print(f"{data}(*{attr}) -> {res}")


class Cache:
    """Redis Class"""

    def __init__(self):
        """constructor"""
        self._redis = Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """returns a string"""
        data = str(uuid.uuid4())
        self._redis.set(data, data)
        return data

    def get(self, data: str, fn: Optional[Callable] = None) ->\
            Union[str, bytes, int, float]:
        """get method"""
        if data:
            res = self._redis.get(data)
            return fn(res) if fn else res
