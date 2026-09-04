"""
Advanced Algorithmic Performance Techniques in Python.

Examines:
1. Binary Search using standard library `bisect` module vs linear search.
2. Efficient queue operations using `collections.deque` vs `list.pop(0)`.
"""

import bisect
from collections import deque
import time


def demonstrate_binary_search() -> None:
    """Compare linear search O(n) vs bisect binary search O(log n) on sorted data."""
    # Sorted list of 10 million elements
    large_sorted_list = list(range(0, 20_000_000, 2))
    target = 15_432_100
    
    # 1. Linear search using 'in' operator - O(n)
    start = time.perf_counter()
    linear_found = target in large_sorted_list
    linear_time = time.perf_counter() - start
    
    # 2. Binary search using bisect - O(log n)
    start = time.perf_counter()
    idx = bisect.bisect_left(large_sorted_list, target)
    bisect_found = (idx < len(large_sorted_list)) and (large_sorted_list[idx] == target)
    bisect_time = time.perf_counter() - start
    
    print("=== Search Comparison ===")
    print(f"Linear Search O(n): {linear_time:.6f}s (Found: {linear_found})")
    print(f"Binary Search O(log n): {bisect_time:.6f}s (Found: {bisect_found})")


def demonstrate_queue_performance() -> None:
    """Compare list.pop(0) O(n) vs deque.popleft() O(1)."""
    items_count = 50_000
    
    # List queue popping from start (O(n) for shift)
    lst_queue = list(range(items_count))
    start = time.perf_counter()
    while lst_queue:
        lst_queue.pop(0)
    list_time = time.perf_counter() - start
    
    # Deque popping from start (O(1) pointer adjustment)
    dq_queue = deque(range(items_count))
    start = time.perf_counter()
    while dq_queue:
        dq_queue.popleft()
    deque_time = time.perf_counter() - start
    
    print("\n=== Queue Pop Comparison ===")
    print(f"List pop(0) O(n): {list_time:.4f}s")
    print(f"Deque popleft() O(1): {deque_time:.4f}s")


if __name__ == "__main__":
    demonstrate_binary_search()
    demonstrate_queue_performance()
