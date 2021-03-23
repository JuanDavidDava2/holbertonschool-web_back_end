#!/usr/bin/python3
""" Basic dictionary
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
        Create a class BasicCache
        that inherits from BaseCaching and is a caching system
    """

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
