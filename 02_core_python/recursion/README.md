# Topic: Recursion & Call Stack Mechanics

## What You Will Learn
- The two fundamental requirements of recursion: **Base Case** and **Recursive Step**.
- Understanding the Python call stack and stack frames.
- Call stack depth limit (`sys.getrecursionlimit()`).
- Tail call limitations in Python.

## Core Concepts
1. **Base Case**: The stopping condition that prevents infinite recursion.
2. **Recursive Step**: Reducing problem size towards base case on each call.

## Syntax
```python
def factorial(n: int) -> int:
    # Base Case
    if n <= 1:
        return 1
    # Recursive Step
    return n * factorial(n - 1)
```

## Next Topic
Next: `regular_expressions` — Pattern matching with `re` module.
