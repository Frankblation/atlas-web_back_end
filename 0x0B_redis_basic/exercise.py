#!/usr/bin/env python3
from functools import wraps
import redis
import uuid
from typing import Union, Callable, Optional


def call_history(method: Callable) -> Callable:
    """Decorator store history of inputs and outputs for particular method."""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper that logs inputs and outputs to Redis."""
        input_key = f"{method.__qualname__}: inputs"
        output_key = f"{method.__qualname__}: outputs"
        # Log the input arguments
        self._redis.rpush(input_key, str(args))
        # Call the original method
        result = method(self, *args, **kwargs)
        # Log the result (output)
        self._redis.rpush(output_key, str(result))
        return result
    return wrapper


def replay(method: Callable):
    """Display the history of calls of a particular function."""
    redis_client = method.__self__._redis
    method_name = method.__qualname__

    input_key = f"{method_name}: inputs"
    output_key = f"{method_name}: outputs"

    # Retrieve inputs and outputs from Redis
    inputs = redis_client.lrange(input_key, 0, -1)
    outputs = redis_client.lrange(output_key, 0, -1)

    print(f"{method_name} was called {len(inputs)} times: ")

    # Pair inputs and outputs, decode from bytes, and print them
    for input_val, output_val in zip(inputs, outputs):
        input_decoded = input_val.decode('utf-8')
        output_decoded = output_val.decode('utf-8')
        print(f"{method_name}(*{input_decoded}) -> {output_decoded}")


class Cache:
    """Cache class for storing data in Redis."""

    def __init__(self):
        """Initialize the Redis client and flush the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in Redis and return the key."""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable]
            = None) -> Union[str, bytes, int, None]:
        """Retrieve data apply a conversion function."""
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """Retrieve data as a string from Redis."""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """Retrieve data as an integer from Redis."""
        return self.get(key, fn=int)
