"""
lru cache
https://leetcode.com/problems/lru-cache/
"""
from collections import OrderedDict


class LRUCache:
    """
    pythonic version using OrderedDict, which is a hash map that also
    remembers insertion order and lets you move an existing key to the
    end in O(1). that's exactly the two operations an LRU cache needs:
    "mark this key as most-recently-used" (move_to_end) and "evict the
    least-recently-used key" (popitem(last=False), which pops from the
    front).
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)  # mark as most recently used
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # evict least recently used


class Node:
    """doubly linked list node for the manual implementation below."""

    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCacheDLL:
    """
    manual doubly linked list + hash map version — this is what
    OrderedDict is doing internally, spelled out explicitly. this is
    the version most interviewers actually want to see, since
    OrderedDict.move_to_end() can feel like "cheating" the problem.

    list is kept ordered oldest -> newest, left to right:
        head <-> LRU ... MRU <-> tail
    (head/tail are dummy sentinel nodes so every real node always has
    a real prev and next, no None-checking special cases needed)
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}  # key -> Node

        self.head = Node()  # dummy, head.next = least recently used
        self.tail = Node()  # dummy, tail.prev = most recently used
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node) -> None:
        """unlink node from wherever it currently sits in the list."""
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert_at_tail(self, node: Node) -> None:
        """insert node right before the tail sentinel (= most recent)."""
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self._remove(node)
        self._insert_at_tail(node)  # mark as most recently used
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self._remove(self.map[key])

        node = Node(key, value)
        self.map[key] = node
        self._insert_at_tail(node)

        if len(self.map) > self.capacity:
            lru = self.head.next          # least recently used = right after dummy head
            self._remove(lru)
            del self.map[lru.key]


if __name__ == "__main__":
    for Cache in (LRUCache, LRUCacheDLL):
        c = Cache(2)
        c.put(1, 1)
        c.put(2, 2)
        print(c.get(1))     # 1
        c.put(3, 3)         # evicts key 2
        print(c.get(2))     # -1
        c.put(4, 4)         # evicts key 1
        print(c.get(1))     # -1
        print(c.get(3))     # 3
        print(c.get(4))     # 4
        print("---")