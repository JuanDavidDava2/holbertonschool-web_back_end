#!/usr/bin/python3
""" FIFO caching"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ Create a class FIFOCache that inherit
        from BaseCaching and is a caching system
    """

    def __init__(self):
        super().__init__()
        self.data = {}
        self.data_in = 0
        self.data_out = 0

    def __pop(self):
        """ pops out of the list
        """
        self.data_out += 1
        key = self.data[self.data_out]
        del self.data[self.data_out], self.cache_data[key]

    def __push(self, key, item):
        """ appends to a list
        """
        if len(self.cache_data) > BaseCaching.MAX_ITEMS - 1:
            print("DISCARD: {}".format(self.data[self.data_out + 1]))
            self.__pop()
        self.cache_data[key] = item
        self.data_in += 1
        self.data[self.data_in] = key

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
            else:
                self.__push(key, item)

    def get(self, key):
        """ Get an item by key
        """
        if key is None or self.cache_data.get(key) is None:
            return None
        if key in self.cache_data:
            res = self.cache_data[key]
            return res
