#!/usr/bin/python3
"""
FIFOCache
:return: cache_data
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache
    :return: cache_data
    """
    def __init__(self):
        """
        init
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """
        put
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_key = self.queue.pop(0)
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}")

        self.queue.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """
        Get
        :return: cache_data
        """
        return self.cache_data.get(key, None)