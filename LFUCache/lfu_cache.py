"""
LFU Cache
"""
# from heapq import *
from collections import defaultdict, OrderedDict
from dataclasses import dataclass
from typing import Optional


class LRUCache:

    @dataclass
    class Entry:
        key: str
        val: int
        freq: int = 1

    def __init__(self, cache_size: int = 0):
        self.cache_size = cache_size
        self.entries = defaultdict(OrderedDict)
        self.cached = dict()
        self.min_freq = 1

    def get(self, key: str) -> Optional[Entry]:
        """If item exists returns Entry"""
        entry = self.cached.get(key, None)
        if entry is not None:
            del self.entries[entry.freq][key]
            if len(self.entries[entry.freq]) == 0:
                del self.entries[entry.freq]
                if entry.freq == self.min_freq:
                    self.min_freq += 1
            entry.freq += 1
            self.entries[entry.freq][key] = entry
        return entry

    def put(self, key: str, val: int) -> Optional[Entry]:
        """Inserts into cache if the entry is not present or updates its value and frequency if is present already."""
        entry = self.get(key)
        if entry is not None:
            entry.val = val
        else:
            if len(self.cached) == self.cache_size:
                o_key, _ = self.entries[self.min_freq].popitem(last=False)
                if len(self.entries[self.min_freq]) == 0:
                    del self.entries[self.min_freq]
                del self.cached[o_key]
            self.min_freq = 1
            entry = self.Entry(key, val)
            self.cached[key] = entry
            self.entries[entry.freq][key] = entry
        return entry


if __name__ == "__main__":
    cache = LRUCache(3)
    cache.put("a", 3)
    cache.put("b", 5)
    cache.put("a", 7)
    cache.put("b", 5)
    cache.put("b", 8)
    cache.put("c", 1)
    cache.put("c", 1)
    cache.put("c", 1)
    cache.put("c", 1)
    print(cache.cached)
    print(cache.entries)
    print(cache.min_freq)


    # h = []
    # heappush(h, (3, 1, 6))
    # heappush(h, (5, 2, 5))
    # heappush(h, (1, 3, 4))
    # heappush(h, (2, 4, 3))
    # heappush(h, (1, 5, 2))
    # print(h)
    # print()
    # n_h = [heappop(h), heappop(h), heappop(h), heappop(h) , heappop(h)]
    # print(n_h)
    exit(0)
