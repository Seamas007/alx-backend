#!/usr/bin/env python3

"""
MRUCache Module
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


class MRUCache(BaseCaching):
    """
    MRUCache class, inherits from BaseCaching
    """
    def __init__(self):
        super().__init__()
        self.queue = OrderedDict()

    def put(self, key, item):
        if key is not None and item is not None:
            if key in self.cache_data:
                # Move the existing key to the end of the queue (most recently used)
                self.queue.move_to_end(key)
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    # Remove the most recently used item (last item in the queue)
                    mru_key = next(reversed(self.queue))
                    self.cache_data.pop(mru_key)
                    self.queue.popitem(last=True)
                    print(f"DISCARD: {mru_key}")

            self.cache_data[key] = item
            self.queue[key] = True

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        # Move the accessed key to the end of the queue (most recently used)
        self.queue.move_to_end(key)
        return self.cache_data[key]
