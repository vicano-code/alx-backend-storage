#!/usr/bin/env python3
"""
Writing strings to Redis:
Create a Cache class to initiate redis storage client and store data
"""
import redis
import uuid
from typing import Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ Decorator count calls """
    name = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper method """
        self._redis.incr(name)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """ Decorator call history """

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wraper function """
        input: str = str(args)
        self._redis.rpush(method.__qualname__ + ":inputs", input)

        output = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ":outputs", output)

        return output

    return wrapper


class Cache:
    """
    Redis Cache class definition

    Methods:
    store: generate random key and store input data with the key
    get: read from redis and recover original type of the data
    """
    def __init__(self):
        """initialize a redis client"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data) -> str:
        """generate a random key (uuid), store the input data in Redis
        using the random key and return the key."""
        # Generate random key
        key = str(uuid.uuid4())

        # store data in redis using key
        self._redis.set(key, data)

        return key

    def get(self, key: str, fn: Optional[Callable] = None):
        """get data from redis using key and convert to original type"""
        data = self._redis.get(key)
        if data is None:
            return None

        # Use callable if provided to transform the data
        if fn is not None:
            return fn(data)

        # otherwise return data as is
        return data

    def get_str(self, key: str) -> Optional[str]:
        """Call get with a function to decode the data as a UTF-8 string"""
        return self.get(key, fn=lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """Call get with a function to convert the data to an integer"""
        try:
            return self.get(key, fn=lambda x: int(x.decode('utf-8')))
        except (ValueError, AttributeError):
            return None
