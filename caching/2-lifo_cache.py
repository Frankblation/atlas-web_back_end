#!/usr/bin/python3
"""Module implementing a LIFO caching system."""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO caching system that inherits from BaseCaching.

    Implements a cache replacement policy where the last item added
    is the first one to be discarded when the cache limit is reached.
    """

    def __init__(self):
        """Initialize the cache and track the order of keys."""
        super().__init__()
        self.stack = []  # List to maintain the order of inserted keys (LIFO)

    def put(self, key, item):
        """Assign the item value to the cache for the given key.

        If the cache exceeds the allowed limit (BaseCaching.MAX_ITEMS),
        the last added key will be discarded.

        Args:
            key (str): the key for the cache.
            item (any): the value to store in the cache.
        """
        if key is None or item is None:
            return

        # If key already exists, update it and move it to the top of the stack
        if key in self.cache_data:
            self.stack.remove(key)
        self.stack.append(key)

        # Add the item to the cache
        self.cache_data[key] = item

        # If cache exceeds the max limit, discard the last added item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Pop the most recent key added (LIFO behavior)
            # -2 ensures the one before the latest is discarded
            last_key = self.stack.pop(-2)
            print(f"DISCARD: {last_key}")
            del self.cache_data[last_key]

    def get(self, key):
        """Return the value linked to the given key.

        Args:
            key (str): the key to retrieve the value for.

        Returns:
            any: the value associated with the key, or None if not found.
        """
        return self.cache_data.get(key, None)
