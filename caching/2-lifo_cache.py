#!/usr/bin/python3
""" LIFO Cache """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO caching system """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.last_key = None  # To keep track of the last inserted key

    def put(self, key, item):
        """ Assign to the cache the item value for the key key """
        if key is None or item is None:
            return

        # Add the item to the cache
        self.cache_data[key] = item

        # Track the most recently added key
        self.last_key = key

        # If cache exceeds the max limit, discard the last added item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            if self.last_key:
                # Remove the last key that was added
                print(f"DISCARD: {self.last_key}")
                del self.cache_data[self.last_key]

    def get(self, key):
        """ Return the value linked to the key """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
