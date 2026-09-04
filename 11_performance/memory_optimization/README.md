# Memory Optimization & `__slots__` in Python

## What You Will Learn
* Optimizing memory footprint using `__slots__` on custom classes.
* Replacing heavy instance dictionaries (`__dict__`) with static slot arrays.
* Memory-efficient data structures (`array.array`, `collections.deque`).
* Generators & Iterators for streaming large data sets without loading everything into RAM.

## Why This Matters
By default, every Python object instance allocates a dynamic `__dict__` dictionary to store instance attributes. When instantiating millions of objects (e.g. data points, ORM rows), `__slots__` reduces memory usage by 40-70%!

## Prerequisites
* Classes (`03_object_oriented_programming/classes_objects`)
* Generators (`02_core_python/generators`)

## Core Concepts

### Using `__slots__`
```python
class PointWithSlots:
    __slots__ = ("x", "y")  # Eliminates instance __dict__!

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
```

## Exercises
See `04_exercises.py` to practice measuring class memory footprint reduction with `__slots__`.
