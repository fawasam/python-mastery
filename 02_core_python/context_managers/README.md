# Topic: Context Managers & `contextlib`

## What You Will Learn
- The context management protocol: `__enter__()` and `__exit__()`.
- Using `contextlib.contextmanager` decorator with generator functions (`yield`).
- Automatic resource cleanup (files, locks, database transactions, timer blocks).
- Handling exceptions inside `__exit__()`.

## Core Concepts
1. **`__enter__()`**: Executes setup before entering the `with` code block. Return value is bound to the `as target` variable.
2. **`__exit__(exc_type, exc_val, exc_tb)`**: Executes cleanup after leaving the `with` block. Returning `True` suppresses exceptions raised within the block.

## Syntax
```python
from contextlib import contextmanager

@contextmanager
def managed_resource():
    print("Setup resource")
    try:
        yield "Resource Object"
    finally:
        print("Cleanup resource")
```

## Next Topic
Next: `recursion` — Call stack, base case, recursive breakdown, and recursion limits.
