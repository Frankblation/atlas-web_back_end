#!/usr/bin/env python3
from functools import wraps
import redis
import uuid
from typing import Union, Callable, Optional


def call_history(method: Callable) -> Callable:
    """Decorator to store the history of inputs and outputs for a particular method."""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        # Create Redis keys for inputs and outputs using method's qualified
        # name
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        # Convert the arguments to a string format and store in Redis using
        # RPUSH
        # Redis only stores strings, bytes, numbers
        self._redis.rpush(input_key, str(args))

        # Call the original method to get the output
        result = method(self, *args, **kwargs)

        # Store the result in Redis in the outputs list
        self._redis.rpush(output_key, str(result))

        # Return the result of the method
        return result

    return wrapper


def replay(method: Callable):
    """Display the history of calls of a particular function."""
    redis_client = method.__self__._redis  # Get the Redis client instance
    method_name = method.__qualname__

    # Create the Redis keys for inputs and outputs
    input_key = f"{method_name}:inputs"
    output_key = f"{method_name}:outputs"

    # Fetch the list of inputs and outputs from Redis
    inputs = redis_client.lrange(input_key, 0, -1)
    outputs = redis_client.lrange(output_key, 0, -1)

    # Print the number of times the method was called
    print(f"{method_name} was called {len(inputs)} times:")

    # Zip inputs and outputs together and print them in the required format
    for input_val, output_val in zip(inputs, outputs):
        print(
            f"{method_name}(*{input_val.decode('utf-8')}) -> {output_val.decode('utf-8')}")


class Cache:
    def __init__(self):
        """Initialize the Redis client and flush the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history  # Only call_history decorator should be here
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
