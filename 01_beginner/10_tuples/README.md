# Topic 10: Tuples, Immutability & Structural Unpacking

## What You Will Learn
- What a tuple is in Python (ordered, immutable sequence).
- Single-element tuple syntax (requires a trailing comma: `(42,)`).
- Tuple packing and unpacking (`x, y, z = coords`).
- Extended iterable unpacking (`head, *tail = items`).
- Memory efficiency and speed advantages of tuples over lists.

## Why This Matters
Tuples protect fixed collections of items from accidental mutation, serve as valid hashable dictionary keys, and allow multiple values to be returned from functions cleanly.

## Core Concepts
1. **Immutability**: Once created, tuple elements cannot be added, removed, or reassigned.
2. **Tuple Syntax**: The trailing comma creates a single-element tuple: `item = (42,)`, not `item = (42)` (which is just an integer in parentheses).
3. **Dictionary Keys**: Because tuples are immutable (hashable), they can be used as keys in dictionaries (e.g. `(latitude, longitude)` coordinates).

## Syntax
```python
# Initialization & Unpacking
point = (10, 20, 30)
x, y, z = point

# Single-element tuple
single_item = ("data",)

# Returning multiple values from function
def get_dimensions():
    return 1920, 1080  # Returns tuple (1920, 1080)
```

## Next Topic
Next: `11_sets` — Unique elements, set operations (union, intersection, difference), and O(1) membership testing.
