#!/usr/bin/python3
"""Module implementing a LIFO caching system."""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO caching system that inherits from BaseCaching.

    Implements a cache replacement policy where the last item added
    is the first one to be discarded when the cache limit is reached.
    """

    def __init__(self):
        """Initialize the cache with an additional attribute to track
        the last inserted key."""
        super().__init__()
        self.last_key = None

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

        # Add the item to the cache
        self.cache_data[key] = item

        # Track the most recently added key
        self.last_key = key

        # If cache exceeds the max limit, discard the last added item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            if self.last_key:
                print(f"DISCARD: {self.last_key}")
                del self.cache_data[self.last_key]

    def get(self, key):
        """Return the value linked to the given key.

        Args:
            key (str): the key to retrieve the value for.

        Returns:
            any: the value associated with the key, or None if not found.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
