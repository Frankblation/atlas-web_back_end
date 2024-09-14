#!/usr/bin/env python3
""" Basic Dictionary Caching Module
"""
from base_caching import BaseCaching  # Corrected import statement


class BasicCache(BaseCaching):
    """Basic caching system without a limit on the number of items"""

    def put(self, key, item):
        """Assign the item to the key in the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Return the value associated with the key in cache"""
        return self.cache_data.get(key)
