#!/usr/bin/python3
""" LRU Caching """

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache class that implements a LRU caching system """

    def __init__(self):
        """ Initialize the class """
        super().__init__()
        self.lru_order = []  # To track the order of access (keys)

    def put(self, key, item):
        """ Add an item to the cache and implement LRU algorithm """
        if key is None or item is None:
            return

        # If key already exists, update the value and move key to most recent
        if key in self.cache_data:
            self.lru_order.remove(key)

        self.cache_data[key] = item
        self.lru_order.append(key)

        # If cache exceeds MAX_ITEMS, discard the least recently used item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            lru_key = self.lru_order.pop(0)  # Remove the first (oldest) key
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")

    def get(self, key):
        """ Get an item by key and update its position in the LRU order """
        if key is None or key not in self.cache_data:
            return None

        # Update the LRU order since this key was recently accessed
        self.lru_order.remove(key)
        self.lru_order.append(key)

        return self.cache_data[key]
