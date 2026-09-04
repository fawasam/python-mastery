"""
Solutions for Caching Exercises.
"""

import functools


@functools.lru_cache(maxsize=128)
def cached_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return cached_fibonacci(n - 1) + cached_fibonacci(n - 2)


if __name__ == "__main__":
    res = cached_fibonacci(40)
    assert res == 102334155
    print(f"Cached fibonacci(40) exercise result: {res}")
