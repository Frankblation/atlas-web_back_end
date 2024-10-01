#!/usr/bin/env python3
import redis
import uuid
from typing import Union


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
