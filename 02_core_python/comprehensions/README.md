# Topic: Comprehensions in Python

## What You Will Learn
- List comprehensions: `[expr for item in iterable if condition]`.
- Set comprehensions: `{expr for item in iterable if condition}`.
- Dictionary comprehensions: `{key_expr: val_expr for item in iterable if condition}`.
- Nested comprehensions and multi-clause filtering.
- Performance benefits of comprehensions over standard `for` loops.

## Why This Matters
Comprehensions are Python's signature construct for concise, expressive, high-performance data transformations.

## Syntax
```python
# List comprehension
evens = [x for x in range(10) if x % 2 == 0]

# Dict comprehension
square_map = {x: x**2 for x in range(5)}

# Set comprehension
unique_lengths = {len(w) for w in ["apple", "banana", "fig"]}
```

## Next Topic
Next: `lambda` — Anonymous inline functions and key sorting expressions.
