# Topic 11: Sets, Uniqueness & Set Operations

## What You Will Learn
- Python sets as unordered, unindexed collections of unique, hashable elements.
- Initializing sets (`{1, 2, 3}` or `set()`). Note: `{}` creates an empty dictionary!
- Set operations:
  - Union (`|` or `.union()`): Combines elements from both sets.
  - Intersection (`&` or `.intersection()`): Elements common to both sets.
  - Difference (`-` or `.difference()`): Elements in first set but not second.
  - Symmetric Difference (`^` or `.symmetric_difference()`): Elements in either set, but not both.
- Fast `O(1)` average time complexity for membership testing (`in` operator).

## Why This Matters
Sets are indispensable for removing duplicates from data pipelines and performing set algebra (e.g. comparing user permissions, checking missing items between datasets).

## Core Concepts
1. **Uniqueness**: Sets automatically eliminate duplicates.
2. **Unordered**: Elements have no defined sequence order or index (`set[0]` raises `TypeError`).
3. **`O(1)` Lookups**: Searching a set takes constant time regardless of set size, whereas searching a list takes `O(n)` linear time.

## Syntax
```python
# Initialization
empty_set = set() # REQUIRED! {} creates a dictionary
numbers = {1, 2, 3, 3, 3} # Deduplicated automatically -> {1, 2, 3}

# Set Math
admin_perms = {"read", "write", "delete"}
user_perms = {"read"}

missing_perms = admin_perms - user_perms # {"write", "delete"}
```

## Next Topic
Next: `12_dictionaries` — Key-value mapping, dict methods, view objects, and nested dicts.
