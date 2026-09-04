# Defensive Programming in Python

## What You Will Learn
* Defensive programming principles (Failing fast, Input validation, Guard clauses).
* Guard clauses to reduce function nesting depth.
* Immutable data patterns and defensive copying.
* Handling edge cases and boundary conditions proactively.

## Why This Matters
Defensive programming minimizes bugs by assuming that external inputs, function arguments, and network responses will occasionally be invalid or malformed. By validating contracts early at function entry points (fail fast), applications stay stable and easy to maintain.

## Prerequisites
* Exceptions & Custom Exceptions (`05_error_handling_debugging/exceptions`, `05_error_handling_debugging/custom_exceptions`)

## Core Concepts

### 1. Guard Clauses & Fail-Fast Principle
Instead of deeply nested `if-else` blocks, validate preconditions immediately at the top of the function and return or raise early.

Bad (Deeply nested):
```python
def process_order(user, cart):
    if user is not None:
        if user.is_active:
            if len(cart) > 0:
                # Do work
                pass
```

Good (Guard Clauses):
```python
def process_order(user, cart):
    if user is None or not user.is_active:
        raise ValueError("Active user required")
    if not cart:
        raise ValueError("Cart cannot be empty")

    # Do work directly without indentation
```

### 2. Defensive Copying
When returning or storing mutable objects (lists, dicts), return copies (`.copy()`) to prevent callers from unexpectedly mutating internal state.

## Exercises
See `04_exercises.py` to practice refactoring nested code into guard clause pipelines.
