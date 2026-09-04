# Custom Exceptions in Python

## What You Will Learn
* Creating domain-specific exception hierarchies inheriting from `Exception`.
* Adding custom context attributes and parameters to exception classes.
* Structuring exception hierarchies for complex modules (base exception vs sub-exceptions).
* Formatting custom error messages via `__str__`.

## Why This Matters
Built-in exceptions like `ValueError` or `KeyError` are generic. Custom exceptions communicate domain business logic errors (e.g. `InsufficientFundsError`, `UserNotFoundError`) to caller code, enabling clear error boundaries.

## Prerequisites
* Classes & Inheritance (`03_object_oriented_programming/inheritance`)
* Exceptions (`05_error_handling_debugging/exceptions`)

## Core Concepts

### Exception Hierarchy Pattern
Always create a single base exception for your library or service, and inherit specific errors from it:

```python
class AppBaseException(Exception):
    """Base exception for all application errors."""
    pass

class ValidationError(AppBaseException):
    """Raised when data validation fails."""
    def __init__(self, field: str, message: str) -> None:
        super().__init__(f"Field '{field}': {message}")
        self.field = field

class NetworkError(AppBaseException):
    """Raised when remote service call fails."""
    pass
```

## Common Mistakes
* **Inheriting from `BaseException` instead of `Exception`**: Breaks catching with `except Exception:`.
* **Not calling `super().__init__()`**: Can prevent standard exception printing or args tuple serialization.

## Exercises
See `04_exercises.py` to practice creating structured error hierarchies for an e-commerce payment system.
