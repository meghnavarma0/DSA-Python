# Design and implement a data structure for LRU (Least Recently Used) cache. It should support the following operations: get and set.

# 1. get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# 2. set(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least recently used item before inserting the new item.
# The LRU Cache will be initialized with an integer corresponding to its capacity. Capacity indicates the maximum number of unique keys it can hold at a time.

# Definition of “least recently used” : An access to an item is defined as a get or a set operation of the item. “Least recently used” item is the one with the oldest access time.
from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key in self.cache:
            temp = self.cache[key]
            del self.cache[key]
            self.cache[key] = temp
            return self.cache[key]
        else:
            return -1

    def set(self, key, value):
        if key in self.cache:
            del self.cache[key]
            
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last = False)
cache = LRUCache(2)  
cache.set(1, 1) 
print(cache.cache) 
cache.set(2, 2) 
print(cache.cache) 
cache.get(1) 
print(cache.cache) 
cache.set(3, 3) 
print(cache.cache) 
cache.get(2) 
print(cache.cache) 
cache.set(4, 4) 
print(cache.cache) 
cache.get(1) 
print(cache.cache) 
cache.get(3) 
print(cache.cache) 
cache.get(4) 
print(cache.cache) 