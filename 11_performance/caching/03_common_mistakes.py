"""
Common Mistakes in Function Caching.
"""

import functools


# MISTAKE 1: Passing unhashable arguments (like list or dict) to @lru_cache
@functools.lru_cache
def mistake_unhashable_args(items: list[int]) -> int:
    # DANGER: Calling mistake_unhashable_args([1, 2, 3]) raises TypeError: unhashable type: 'list'!
    # Function arguments MUST be hashable (e.g. tuples instead of lists, frozenset instead of set)!
    return sum(items)


if __name__ == "__main__":
    try:
        mistake_unhashable_args([1, 2, 3])  # Unhashable list passed!
    except TypeError as err:
        print(f"Caught Unhashable Argument Error: {err}")
