#!/usr/bin/env python3

"""
LFUCache Module
"""

from collections import OrderedDict, defaultdict

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


class LFUCache(BaseCaching):
    """
    LFUCache class, inherits from BaseCaching
    """
    def __init__(self):
        super().__init__()
        self.freq_counter = defaultdict(int)
        self.queue = OrderedDict()

    def put(self, key, item):
        if key is not None and item is not None:
            if key in self.cache_data:
                # Move the existing key to the end of the queue (most recently used)
                self.queue.move_to_end(key)
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    # Find the least frequency used items
                    min_freq = min(self.freq_counter.values())
                    least_frequent_keys = [k for k, v in self.freq_counter.items() if v == min_freq]

                    # If there is more than one item with the least frequency,
                    # use the LRU algorithm to select the least recently used item
                    lru_key = next(iter(self.queue))
                    for key in least_frequent_keys:
                        if key in self.queue:
                            lru_key = key
                            break

                    self.cache_data.pop(lru_key)
                    self.queue.pop(lru_key)
                    print(f"DISCARD: {lru_key}")

            self.cache_data[key] = item
            self.queue[key] = True
            self.freq_counter[key] += 1

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        # Move the accessed key to the end of the queue (most recently used)
        self.queue.move_to_end(key)
        self.freq_counter[key] += 1
        return self.cache_data[key]
