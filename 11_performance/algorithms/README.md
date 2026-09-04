# Algorithmic Complexity and Optimization

## What You Will Learn
- Understanding Big-O notation ($\mathcal{O}(1)$, $\mathcal{O}(\log n)$, $\mathcal{O}(n)$, $\mathcal{O}(n \log n)$, $\mathcal{O}(n^2)$)
- Time vs Space complexity trade-offs
- Selecting optimal data structures (dicts/sets vs lists) for operations
- Efficient algorithm design patterns (Two pointers, Sliding window, Memoization)

## Why This Matters
Algorithm choice is often the single biggest factor in Python program performance. An $O(n^2)$ algorithm processing 100,000 items takes hours, while an $O(n \log n)$ or $O(n)$ implementation takes less than a second.

## Prerequisites
- Basic Data Structures (Lists, Dictionaries, Sets)
- Functions and Recursion basics

## Core Concepts

### Time Complexity (Big-O Notation)
- **$\mathcal{O}(1)$ Constant time**: Dictionary lookup `d[key]`, set membership `x in s`.
- **$\mathcal{O}(\log n)$ Logarithmic**: Binary search in sorted list.
- **$\mathcal{O}(n)$ Linear**: Single loop over $n$ items, list search `x in lst`.
- **$\mathcal{O}(n \log n)$ Linearithmic**: Sorting using `sorted()` or `list.sort()`.
- **$\mathcal{O}(n^2)$ Quadratic**: Nested loops over $n$ items.

### Data Structure Complexity Comparison
| Operation | List | Set | Dict |
|---|---|---|---|
| Search (`x in container`) | $O(n)$ | $O(1)$ average | $O(1)$ average |
| Append / Insert | $O(1)$ end / $O(n)$ start | $O(1)$ average | $O(1)$ average |
| Delete | $O(n)$ | $O(1)$ average | $O(1)$ average |

## Examples

See `01_basic.py` and `02_examples.py` for runnable code demonstrating algorithmic optimizations.

## Common Mistakes
1. Using `in` operator inside a loop on a list instead of converting to a set first (turning $O(n)$ into $O(n^2)$).
2. Repeatedly concatenating strings with `+` inside a loop instead of `str.join()`.
3. Re-sorting data unnecessarily when maintaining insertion order or using heap/bisect would suffice.

## Best Practices
- Prefer sets/dictionaries for membership lookups.
- Use `bisect` for fast lookups in pre-sorted lists.
- Use `collections.deque` for FIFO queues (O(1) pops from front vs O(n) for lists).

## Exercises
Complete exercises in `04_exercises.py` and check your answers in `05_solution.py`.

## Next Topic
Complete the Performance Mini Project in `../mini_project/`.
