#!/usr/bin/python3
""" BaseCaching module
"""
from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """Basic caching system without a limit"""

    def put(self, key, item):
        """Assign the item value to the key in the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Return the value associated with the key in cache"""
        return self.cache_data.get(key, None)