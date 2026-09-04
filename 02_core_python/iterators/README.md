# Topic: Iterators & The Iteration Protocol

## What You Will Learn
- The Python Iteration Protocol: `__iter__()` and `__next__()`.
- Difference between an **Iterable** (an object with `__iter__` returning an iterator) and an **Iterator** (an object with `__next__` returning items until `StopIteration`).
- Built-in functions `iter()` and `next()`.
- Building custom iterator classes from scratch.

## Core Concepts
1. **Iterable**: Lists, tuples, strings, dicts are iterables. Passing them to `iter(obj)` returns an iterator.
2. **Iterator**: Remembers state during iteration. Calling `next(iterator)` returns the next item. When exhausted, raises `StopIteration`.

## Syntax
```python
class CountDown:
    def __init__(self, start: int):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        val = self.current
        self.current -= 1
        return val
```

## Next Topic
Next: `generators` — Memory-efficient data streams using `yield`.
