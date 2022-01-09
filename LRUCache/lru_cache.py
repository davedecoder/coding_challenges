"""You have a Stream of data that is stored in a cache array of fixed size.
The LRU caching scheme is to remove the least recently used frame when the cache
is full and a new page is referenced which is not there in cache.
"""

from typing import List


class Node:
    def __init__(self, item, prv=None, nxt=None):
        self.item = item
        self.prv = prv
        self.nxt = nxt


class LRUCache:
    def __init__(self, cache_size):
        self._cache_size = cache_size
        self._cached = {}
        self.head: (Node, None) = None
        self.tail:(Node, None) = None

    def print_cache(self):
        node = self.head
        while node is not None:
            print(node.item)
            node = node.nxt

    def get_cache(self) -> List[str]:
        cached = []
        node = self.head
        while node is not None:
            cached.append(node.item)
            node = node.nxt
        return cached

    def _add(self, item: str):
        if len(self._cached) == 0:
            node = Node(item)
            self.head = node
            self.tail = node
        elif len(self._cached) == self._cache_size:
            # chop tail and add to head
            least = self.tail
            self.tail = least.prv
            self.tail.nxt = None
            del self._cached[least.item]

            least = self.head
            node = Node(item, nxt=least)
            least.prv = node
            self.head = node
        else:
            least = self.head
            node = Node(item, nxt=least)
            least.prv = node
            self.head = node

        self._cached[item] = node

    def _re_order(self, item):
        node = self._cached[item]
        if self.head == node:
            return
        prev_node = node.prv
        next_node = node.nxt
        if self.tail == node:
            prev_node.nxt = next_node
            self.tail = prev_node
        else:
            prev_node.nxt = next_node
            next_node.prv = prev_node

        least = self.head
        least.prv = node
        node.nxt = least
        node.prv = None
        self.head = node

    def insert_item(self, item: str) -> List[str]:
        if self._cached.get(item, None) is None:
            self._add(item)
        else:
            self._re_order(item)
        return self.get_cache()



if __name__ == "__main__":
    cache_size = 3
    s = LRUCache(cache_size)
    assert s.get_cache() == []
    incoming_stream = ["A", "B", "C", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "B", "C", "D"]
    actual_cache = s.insert_item("A")
    assert actual_cache == ["A"]
    actual_cache = s.insert_item("A")
    assert actual_cache == ["A"]
    actual_cache = s.insert_item("B")
    assert actual_cache == ["B", "A"]
    actual_cache = s.insert_item("A")
    assert actual_cache == ["A", "B"]
    actual_cache = s.insert_item("B")
    assert actual_cache == ["B", "A"]
    actual_cache = s.insert_item("A")
    assert actual_cache == ["A", "B"]
    actual_cache = s.insert_item("C")
    assert actual_cache == ["C", "A", "B"]
    actual_cache = s.insert_item("B")
    assert actual_cache == ["B", "C", "A"]
    actual_cache = s.insert_item("D")
    assert actual_cache == ["D", "B", "C"]
    actual_cache = s.insert_item("C")
    assert actual_cache == ["C", "D", "B"]
    actual_cache = s.insert_item("D")
    assert actual_cache == ["D", "C", "B"]
    actual_cache = s.insert_item("D")
    assert actual_cache == ["D", "C", "B"]
    for item in incoming_stream:
        s.insert_item(item)
    actual_cache = s.get_cache()
    assert actual_cache == ["D", "C", "B"]

    print("Done!")

