#!/usr/bin/python3
""" Basic Dictionary
"""


class BaseCaching:
    """ Base caching class """

    def __init__(self):
        """ Initialize the cache """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache """
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data[key]))

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key)

    