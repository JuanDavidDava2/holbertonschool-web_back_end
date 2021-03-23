#!/usr/bin/python3
""" LRU Caching
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ Create a class LRUCache that inherits
        from BaseCaching and is a caching system
    """

    def __init__(self):
        super().__init__()
        self.head, self.tail = '-', '='
        self.next, self.prev = {}, {}
        self.__group(self.head, self.tail)

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            if key in self.cache_data:
                self.__remove(key)
            self.__add(key, item)

    def __remove(self, key):
        """ Remove an item from the cache
        """
        self.__group(self.prev[key], self.next[key])
        del self.prev[key], self.next[key], self.cache_data[key]

    def __group(self, x, y):
        """ Group items
        """
        self.next[x], self.prev[y] = y, x

    def __add(self, key, item):
        """ Add an item in the cache
        """
        self.cache_data[key] = item
        self.__group(self.prev[self.tail], key)
        self.__group(key, self.tail)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            print("DISCARD: {}".format(self.next[self.head]))
            self.__remove(self.next[self.head])

    def get(self, key):
        """ Get an item by key
        """
        if key is None or self.cache_data.get(key) is None:
            return None
        if key in self.cache_data:
            data = self.cache_data[key]
            self.__remove(key)
            self.__add(key, data)
            return data
