#!/usr/bin/python3
""" MRU Caching """

from base_caching import BaseCaching

class MRUCache(BaseCaching):
    """ MRUCache class that implements a MRU caching system """

    def __init__(self):
        """ Initialize the class """
        super().__init__()
        self.mru_order = []  # To track the most recent access (keys)

    def put(self, key, item):
        """ Add an item to the cache using MRU algorithm """
        if key is None or item is None:
            return

        # If the key already exists, update it and move it to most recent
        if key in self.cache_data:
            self.mru_order.remove(key)
        else:
            # Check if we need to discard the most recently used item
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Discard the most recently used item
                mru_key = self.mru_order.pop()  # Get the last used key
                del self.cache_data[mru_key]
                print(f"DISCARD: {mru_key}")

        # Add the new item to the cache and update the MRU order
        self.cache_data[key] = item
        self.mru_order.append(key)

    def get(self, key):
        """ Get an item by key and mark it as recently used """
        if key is None or key not in self.cache_data:
            return None

        # Update the MRU order since this key was recently accessed
        self.mru_order.remove(key)
        self.mru_order.append(key)
        
        return self.cache_data[key]
