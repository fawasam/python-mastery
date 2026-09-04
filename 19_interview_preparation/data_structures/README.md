# Data Structures Interview Preparation Guide

## Core Python Data Structures & Complexity

| Data Structure | Access | Search | Insertion | Deletion | Space |
|---|---|---|---|---|---|
| **Array / List** | $\mathcal{O}(1)$ | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ |
| **Hash Map / Dict** | $\mathcal{O}(1)$ avg | $\mathcal{O}(1)$ avg | $\mathcal{O}(1)$ avg | $\mathcal{O}(1)$ avg | $\mathcal{O}(n)$ |
| **Set** | N/A | $\mathcal{O}(1)$ avg | $\mathcal{O}(1)$ avg | $\mathcal{O}(1)$ avg | $\mathcal{O}(n)$ |
| **Stack (List / Deque)** | $\mathcal{O}(1)$ top | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ | $\mathcal{O}(n)$ |
| **Queue (Deque)** | $\mathcal{O}(1)$ front | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ | $\mathcal{O}(n)$ |
| **Binary Search Tree** | $\mathcal{O}(\log n)$ avg | $\mathcal{O}(\log n)$ avg | $\mathcal{O}(\log n)$ avg | $\mathcal{O}(\log n)$ avg | $\mathcal{O}(n)$ |
| **Heap (Priority Queue)** | $\mathcal{O}(1)$ min | $\mathcal{O}(n)$ | $\mathcal{O}(\log n)$ | $\mathcal{O}(\log n)$ | $\mathcal{O}(n)$ |

## Python Implementation Highlights

### Singly Linked List Implementation
```python
class ListNode:
    def __init__(self, val: int = 0, next_node: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next_node

def reverse_list(head: ListNode | None) -> ListNode | None:
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev
```

### Trie (Prefix Tree) Implementation
```python
class TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.is_end_of_word: bool = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.children.setdefault(char, TrieNode())
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word
```
