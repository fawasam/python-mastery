"""
Algorithmic Performance Basics: Demonstrating Time Complexity Differences.

This file compares O(n^2) naive lookup algorithms against O(n) optimized algorithms using sets.
"""

import time


def find_duplicates_slow(items: list[int]) -> list[int]:
    """
    Find duplicate elements using nested lists (O(n^2) complexity).
    
    Why: Checking 'item in duplicates' and list membership causes scanning through the list
    for every element, resulting in quadratic time execution.
    """
    duplicates: list[int] = []
    seen: list[int] = []
    
    for item in items:
        # Checking 'item in seen' takes O(n) time on a list
        if item in seen and item not in duplicates:
            duplicates.append(item)
        seen.append(item)
        
    return duplicates


def find_duplicates_fast(items: list[int]) -> list[int]:
    """
    Find duplicate elements using hash sets (O(n) complexity).
    
    Why: Set lookup 'item in seen' runs in O(1) average time, making the entire function O(n).
    """
    duplicates: set[int] = set()
    seen: set[int] = set()
    
    for item in items:
        # Hash set membership check takes O(1) time
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
            
    return list(duplicates)


if __name__ == "__main__":
    # Generate test dataset
    data = list(range(10000)) + list(range(5000))  # 15,000 items with duplicates
    
    start = time.perf_counter()
    slow_res = find_duplicates_slow(data)
    slow_time = time.perf_counter() - start
    print(f"O(n^2) List Method Time: {slow_time:.4f} seconds (Found {len(slow_res)} duplicates)")
    
    start = time.perf_counter()
    fast_res = find_duplicates_fast(data)
    fast_time = time.perf_counter() - start
    print(f"O(n) Set Method Time:  {fast_time:.4f} seconds (Found {len(fast_res)} duplicates)")
    
    if slow_time > 0:
        print(f"Speedup ratio: {slow_time / fast_time:.1f}x faster!")
