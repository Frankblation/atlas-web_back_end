#!/usr/bin/env python3
from functools import wraps
import redis
import uuid
from typing import Union, Callable, Optional


def count_calls(method: Callable) -> Callable:
    """Decorator that counts how many times a method is called."""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__  # Get the qualified name of the method
        self._redis.incr(key)  # Increment the call count for the method
        return method(self, *args, **kwargs)  # Call the original method
    return wrapper


class Cache:
    def __init__(self):
        """Initialize the Redis client and flush the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls  # Decorate the store method with count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store the data in Redis and return the key."""
        key = str(uuid.uuid4())  # Generate a random UUID key
        self._redis.set(key, data)  # Store the data in Redis
        return key

    def get(self, key: str, fn: Optional[Callable]
            = None) -> Union[str, bytes, int, None]:
        """Retrieve data from Redis, optionally converting it using fn."""
        data = self._redis.get(key)
        if data is None:
            return None  # If the key does not exist, return None
        if fn is not None:
            return fn(data)  # Apply the conversion function if provided
        return data  # Return raw data if no conversion function is provided

    def get_str(self, key: str) -> Optional[str]:
        """Retrieve a string from Redis."""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """Retrieve an integer from Redis."""
        return self.get(key, fn=int)
