#!/usr/bin/python3
""" FIFOCache module """

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO caching system class """

    def __init__(self):
        """ Initialize the class """
        super().__init__()
        self.order = []  # Keep track of the order of keys

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        # If key is already in cache, update it and move it to the end of the
        # order list
        if key in self.cache_data:
            self.order.remove(key)
        else:
            # Check if the cache is full and remove the first added item (FIFO)
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded = self.order.pop(0)
                del self.cache_data[discarded]
                print(f"DISCARD: {discarded}")

        # Add the key-item pair to cache and update the order
        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
