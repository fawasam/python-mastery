# Python Coding Interview Problems & Top Patterns

## Problem Patterns Overview
1. Two Pointers
2. Sliding Window
3. Fast & Slow Pointers
4. Subsets & Backtracking
5. Monotonic Stack
6. Top-K Elements / Heaps
7. Dynamic Programming

---

### Problem 1: Two Sum (Hash Map Pattern)

**Difficulty:** ⭐ Easy | **Time:** $O(n)$ | **Space:** $O(n)$

**Problem Statement:**
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

```python
def two_sum(nums: list[int], target: int) -> list[int]:
    seen: dict[int, int] = {}
    for idx, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], idx]
        seen[num] = idx
    return []

# Test
print(two_sum([2, 7, 11, 15], 9))  # Output: [0, 1]
```

---

### Problem 2: Longest Substring Without Repeating Characters (Sliding Window Pattern)

**Difficulty:** ⭐⭐ Medium | **Time:** $O(n)$ | **Space:** $O(k)$

**Problem Statement:**
Given a string `s`, find the length of the longest substring without repeating characters.

```python
def length_of_longest_substring(s: str) -> int:
    char_index_map: dict[str, int] = {}
    left = 0
    max_length = 0
    
    for right, char in enumerate(s):
        if char in char_index_map and char_index_map[char] >= left:
            left = char_index_map[char] + 1
        char_index_map[char] = right
        max_length = max(max_length, right - left + 1)
        
    return max_length

# Test
print(length_of_longest_substring("abcabcbb"))  # Output: 3 ("abc")
```

---

### Problem 3: Valid Parentheses (Stack Pattern)

**Difficulty:** ⭐ Easy | **Time:** $O(n)$ | **Space:** $O(n)$

```python
def is_valid_parentheses(s: str) -> bool:
    stack: list[str] = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping:
            top = stack.pop() if stack else "#"
            if mapping[char] != top:
                return False
        else:
            stack.append(char)
    return not stack

# Test
print(is_valid_parentheses("()[]{}"))  # Output: True
```

---

### Problem 4: Merge K Sorted Lists (Min-Heap Pattern)

**Difficulty:** ⭐⭐⭐ Hard | **Time:** $O(N \log k)$ | **Space:** $O(k)$

```python
import heapq

def merge_k_sorted_lists(lists: list[list[int]]) -> list[int]:
    min_heap: list[tuple[int, int, int]] = []
    for list_idx, lst in enumerate(lists):
        if lst:
            heapq.heappush(min_heap, (lst[0], list_idx, 0))
            
    merged: list[int] = []
    while min_heap:
        val, list_idx, element_idx = heapq.heappop(min_heap)
        merged.append(val)
        if element_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][element_idx + 1]
            heapq.heappush(min_heap, (next_val, list_idx, element_idx + 1))
            
    return merged

# Test
print(merge_k_sorted_lists([[1, 4, 5], [1, 3, 4], [2, 6]]))  # Output: [1, 1, 2, 3, 4, 4, 5, 6]
```
