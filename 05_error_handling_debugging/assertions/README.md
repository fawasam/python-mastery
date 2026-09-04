# Assertions in Python

## What You Will Learn
* The `assert` statement syntax and behavior.
* Using assertions for internal sanity checks and invariants.
* Why assertions are disabled in optimized Python (`python -O`).
* Differentiating between user input validation and assertion invariants.

## Why This Matters
Assertions are developer internal checks. They document assumptions in your code (e.g., "this list should never be empty at this step") and raise `AssertionError` if an internal bug violates those assumptions during development and testing.

## Prerequisites
* Exception Handling (`05_error_handling_debugging/exceptions`)

## Core Concepts

### Syntax
```python
assert condition, "Error message if condition evaluates to False"
```

### When to Use Assertions
- Checking internal state invariants inside private functions.
- Validating function argument preconditions during internal debugging.

### When NOT to Use Assertions
- Data validation for public APIs or user input.
- Security and authorization checks.
(Because running Python with the `-O` optimization flag strips all `assert` statements from bytecode!).

## Common Mistakes
* **Using tuple syntax in assertions**: `assert (val > 0, "Error")` evaluates a non-empty 2-tuple, which ALWAYS evaluates to `True` regardless of `val > 0`!

## Exercises
See `04_exercises.py` to practice writing assertion invariant checks.
