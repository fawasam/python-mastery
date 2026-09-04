# Topic 12: Dictionaries, Key-Value Mappings & Nested Structures

## What You Will Learn
- Python dictionaries (`dict`) as mutable, ordered key-value mappings (Insertion ordered since Python 3.7+).
- Accessing & modifying keys: `dict[key]`, `dict.get(key, default)`, `dict.setdefault()`.
- Essential dict methods: `.keys()`, `.values()`, `.items()`, `.pop()`, `.update()`.
- Dictionary view objects dynamic behavior.
- Working with complex nested dictionaries (JSON-like structures).

## Why This Matters
Dictionaries are foundational to Python programming. APIs, JSON payloads, configurations, object attributes, and fast `O(1)` hash table lookups rely on Python dictionaries.

## Core Concepts
1. **Keys Must Be Hashable**: Keys must be immutable types (`str`, `int`, `float`, `tuple`). Values can be *any* object.
2. **Safe Retrieval with `.get()`**: Avoids `KeyError` exceptions when retrieving optional keys.
3. **Dictionary Views**: `.keys()`, `.values()`, and `.items()` return dynamic view objects that reflect dictionary modifications automatically.

## Syntax
```python
user = {
    "id": 1001,
    "name": "Sarah",
    "roles": ["admin", "developer"],
}

# Safe lookup with default fallback
status = user.get("status", "INACTIVE")

# Iterating over key-value pairs
for key, val in user.items():
    print(f"{key}: {val}")
```

## Next Topic
Next: `13_functions` — Function definitions, parameters, return types, default arguments, `*args`, and `**kwargs`.
