# Topic 09: Lists, Mutability & Operations

## What You Will Learn
- Python lists as dynamic, ordered, mutable sequences.
- Adding elements: `.append()`, `.extend()`, `.insert()`.
- Removing elements: `.pop()`, `.remove()`, `clear()`, `del`.
- Searching & ordering: `.index()`, `.count()`, `.sort()`, `.reverse()`, `sorted()`.
- Reference semantics: Shallow copy (`list.copy()`, `list[:]`) vs Deep copy (`copy.deepcopy()`).

## Why This Matters
Lists are Python's primary sequence data structure. Understanding mutability and in-place sorting vs returning a new sorted list is critical for bug-free algorithm implementation.

## Core Concepts
1. **Mutable Sequence**: Lists can be modified after creation (elements added, removed, or reassigned).
2. **In-place Methods vs New Objects**:
   - `numbers.sort()` sorts in-place and returns `None`.
   - `sorted(numbers)` leaves `numbers` untouched and returns a *new* sorted list.
3. **Reference Copies**: `b = a` creates a alias to the SAME list object in memory! Modifying `b` will modify `a`.

## Syntax
```python
fruits = ["apple", "banana"]
fruits.append("cherry")      # In-place addition
fruits.extend(["date", "fig"])# Append items from another iterable

# Shallow copy
fruits_copy = fruits.copy()
```

## Next Topic
Next: `10_tuples` — Immutable sequences, packing, unpacking, and efficiency.
