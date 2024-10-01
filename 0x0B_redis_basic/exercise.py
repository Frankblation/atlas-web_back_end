#!/usr/bin/env python3
import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    def __init__(self):
        """
        Initialize Redis client and flush the database
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis using a randomly generated key.
        :param data: The data to be stored (can be str, bytes, int, or float)
        :return: The generated key as a string
        """
        key = str(uuid.uuid4())  # Generate a random UUID key
        self._redis.set(key, data)  # Store the data in Redis
        return key

    def get(self, key: str, fn: Optional[Callable]
            = None) -> Union[str, bytes, int, None]:
        """
        Retrieve data from Redis and optionally apply a conversion function.
        :param key: The key used to retrieve the data
        :param fn: Optional Callable to convert the data format
        :return: The retrieved data, converted if `fn` is provided
        """
        data = self._redis.get(key)
        if data is None:
            return None  # If key does not exist, return None
        if fn is not None:
            return fn(data)  # Apply the conversion function if provided
        return data  # Return raw data if no conversion function is provided

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve data from Redis and automatically decode it as UTF-8 string.
        :param key: The key used to retrieve the data
        :return: The decoded string, or None if key does not exist
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve data from Redis and automatically convert it to an integer.
        :param key: The key used to retrieve the data
        :return: The converted integer, or None if key does not exist
        """
        return self.get(key, fn=int)
