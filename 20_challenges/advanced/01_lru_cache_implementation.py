"""
Challenge 01: LRU Cache Implementation

Difficulty: ⭐⭐⭐⭐
Topics: Doubly Linked List, Hash Map, OOP

Problem:
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
Must support get(key) and put(key, value) in O(1) average time complexity.
"""


class Node:
    def __init__(self, key: int = 0, val: int = 0) -> None:
        self.key = key
        self.val = val
        self.prev: Node | None = None
        self.next: Node | None = None


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache: dict[int, Node] = {}
        
        # Dummy head and tail nodes
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node) -> None:
        p, n = node.prev, node.next
        if p and n:
            p.next = n
            n.prev = p

    def _add_to_head(self, node: Node) -> None:
        node.next = self.head.next
        node.prev = self.head
        if self.head.next:
            self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add_to_head(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self._add_to_head(node)
        
        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            if lru and lru != self.head:
                self._remove(lru)
                del self.cache[lru.key]


if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 100)
    cache.put(2, 200)
    print("Get 1:", cache.get(1))  # Returns 100
    cache.put(3, 300)             # Evicts key 2
    print("Get 2 (Evicted):", cache.get(2))  # Returns -1
