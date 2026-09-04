# Topic: Map, Filter & Reduce

## What You Will Learn
- `map(func, iterable)`: Applying a transformation function lazily to every item.
- `filter(func, iterable)`: Keeping items where boolean function returns `True`.
- `functools.reduce(func, iterable, initializer)`: Accumulating sequence items down to a single aggregate result value.
- Comparing functional primitives (`map`/`filter`) vs Pythonic comprehensions.

## Core Concepts
1. **Lazy Iterators**: Both `map()` and `filter()` return lazy iterator objects in Python 3, consuming memory only when iterated over.
2. **`functools.reduce()`**: Applies rolling computation to pairs of items (e.g. calculating product or custom reduction).

## Syntax
```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# map: double values
doubles = list(map(lambda x: x * 2, numbers))

# filter: keep evens
evens = list(filter(lambda x: x % 2 == 0, numbers))

# reduce: product sum
product = reduce(lambda acc, val: acc * val, numbers, 1)
```

## Next Topic
Next: `unpacking` — Positional unpacking, starred unpacking (`*rest`), and dictionary merging (`**`).
