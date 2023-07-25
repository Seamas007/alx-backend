#!/usr/bin/env python3

"""
LIFOCache Module
"""

from collections import OrderedDict

class BaseCaching:
    """
    BaseCaching class
    """
    MAX_ITEMS = 4

    def __init__(self):
        self.cache_data = {}

    def print_cache(self):
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        error_msg = "put must be implemented in your cache class"
        raise NotImplementedError(error_msg)

    def get(self, key):
        error_msg = "get must be implemented in your cache class"
        raise NotImplementedError(error_msg)


class LIFOCache(BaseCaching):
    """
    LIFOCache class, inherits from BaseCaching
    """
    def __init__(self):
        super().__init__()
        self.queue = OrderedDict()

    def put(self, key, item):
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                last_key = list(self.queue.keys())[-1]
                self.queue.pop(last_key)
                self.cache_data.pop(last_key)
                print(f"DISCARD: {last_key}")
            self.cache_data[key] = item
            self.queue[key] = True

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
