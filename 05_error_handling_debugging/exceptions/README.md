# Error Handling & Exceptions in Python

## What You Will Learn
* Exception hierarchy in Python (`BaseException` -> `Exception`).
* `try`, `except`, `else`, and `finally` block semantics.
* Catching multiple specific exception types.
* Exception chaining with `raise ... from ...`.
* Extracting exception context (`__cause__`, `__context__`).

## Why This Matters
Unhandled exceptions crash applications. Proper exception handling ensures your application degrades gracefully, cleans up resources (file handles, database connections), and provides meaningful diagnostic feedback when runtime failures occur.

## Prerequisites
* Core Python (`01_beginner/16_exceptions`)

## Core Concepts

### Exception Handling Structure
```python
try:
    # Code that might raise an exception
    result = 10 / divisor
except ZeroDivisionError as e:
    # Executed if ZeroDivisionError occurs
    print(f"Error: {e}")
except (TypeError, ValueError) as e:
    # Catching multiple exception types
    print(f"Invalid input: {e}")
else:
    # Executed ONLY if NO exception was raised in try block
    print(f"Calculation succeeded: {result}")
finally:
    # ALWAYS executed (even if exceptions occur or returns are hit)
    print("Cleanup completed.")
```

### Exception Chaining
```python
try:
    parse_raw_data()
except KeyError as err:
    raise DataValidationError("Missing required field") from err
```

## Common Mistakes
* **Bare `except:` clause**: Catches system-exiting exceptions like `KeyboardInterrupt` and `SystemExit`, making programs hard to terminate.
* **Swallowing exceptions**: Catching an exception without logging or handling it hides bugs and makes troubleshooting impossible.

## Exercises
See `04_exercises.py` to practice writing robust fallback wrappers and exception translation handlers.
