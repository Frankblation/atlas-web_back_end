#!/usr/bin/python3
""" LIFO """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO caching system."""

    def __init__(self):
        """Initialize the LIFO cache."""
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """Add an item to the LIFO cache.

        Args:
            key (str): The key of the item.
            item (any): The item to be added.
        """

        if key is None or item is None:
            return

        self.cache_data[key] = item
        self.last_key = key

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            to_discard = self.last_key
            del self.cache_data[to_discard]
            print("DISCARD:", to_discard)

    def get(self, key):
        """Retrieve an item from the LIFO cache.

        Args:
            key (str): The key of the item.

        Returns:
            The item corresponding to the key, or None if not found.
        """

        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
