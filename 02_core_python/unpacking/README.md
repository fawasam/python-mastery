# Topic: Advanced Unpacking & Dictionary Merging

## What You Will Learn
- Positional unpacking of tuples, lists, and iterables.
- Extended starred unpacking (`first, *middle, last = items`).
- Starred function argument unpacking (`*args` for iterables).
- Double-starred dictionary unpacking (`**kwargs` and `{**dict1, **dict2}`).
- Dictionary union operator in Python 3.9+ (`dict1 | dict2`).

## Syntax
```python
# Extended unpacking
a, *b, c = [1, 2, 3, 4, 5]  # a=1, b=[2, 3, 4], c=5

# Dictionary merging (Python 3.9+)
merged_dict = dict1 | dict2
```

## Next Topic
Next: `iterators` — Iteration protocol (`__iter__`, `__next__`, `iter()`, `next()`).
