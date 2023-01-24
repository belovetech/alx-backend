#!/usr/bin/env python3
"""Class representation of FIFO caching
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache that inherits from BaseCaching
    """
    def __init__(self):
        """Initialize FIFO caching
        """
        super().__init__()

    def put(self, key, item):
        """Assign key and item to the cache system
        """
        if len(self.cache_data) >= self.MAX_ITEMS \
           and key not in self.cache_data.keys():
            # first_key = list(self.cache_data.keys())[0]
            # Getting first key in dictionary using next() + iter()
            first_key = next(iter(self.cache_data))
            del self.cache_data[first_key]
            print("DISCARD: {}".format(first_key))
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Fetch data from the cache system with key
        """
        if not key or key in self.cache_data.keys():
            return None

        return self.cache_data.get(key)
