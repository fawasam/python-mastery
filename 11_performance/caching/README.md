# Memoization & Caching (`functools.lru_cache`) in Python

## What You Will Learn
* In-memory memoization using `functools.lru_cache` and `functools.cache`.
* Least Recently Used (LRU) cache eviction policies (`maxsize`).
* Inspecting cache telemetry (`func.cache_info()`, `func.cache_clear()`).
* TTL (Time-To-Live) custom cache decorators.

## Why This Matters
Caching memoizes previous function returns so that identical future inputs skip expensive recalculation or I/O calls, returning the cached result instantly in O(1) time.

## Prerequisites
* Decorators (`02_core_python/decorators`)

## Core Concepts

### `@functools.lru_cache`
```python
import functools

@functools.lru_cache(maxsize=128)
def fibonacci(n: int) -> int:
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(50))  # Instantaneous O(N) calculation via memoization!
print(fibonacci.cache_info())  # Hits, Misses, Maxsize, Currsize
```

## Exercises
See `04_exercises.py` to practice applying LRU caching to recursive functions.
