#!/usr/bin/env python3

"""
BasicCache Module
"""

class BaseCaching:
    """
    BaseCaching class
    """
    def __init__(self):
        self.cache_data = {}

    def print_cache(self):
        """
        Print the current cache items
        """
        print("Current cache:")
        for key, value in self.cache_data.items():
            print(f"{key}: {value}")


class BasicCache(BaseCaching):
    """
    BasicCache class, inherits from BaseCaching
    """
    def put(self, key, item):
        """
        Put a key-value pair into the cache_data dictionary.

        Args:
            key: Key to be added.
            item: Value to be associated with the key.

        If key or item is None, this method should not do anything.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get the value associated with the given key from cache_data.

        Args:
            key: Key to retrieve the value for.

        Returns:
            The value associated with the key or None if the key doesn't exist.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
