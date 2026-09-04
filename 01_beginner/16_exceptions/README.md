# Topic 16: Exception Handling (try, except, else, finally)

## What You Will Learn
- Python's exception handling mechanism (`try`, `except`, `else`, `finally`).
- Catching specific built-in exception types (`ValueError`, `ZeroDivisionError`, `KeyError`, `TypeError`, `FileNotFoundError`).
- Exception object inspection using `except Exception as err:`.
- The purpose of the `else` block (executes ONLY when NO exceptions were raised inside `try`).
- The purpose of the `finally` block (executes ALWAYS, ideal for cleanup).

## Why This Matters
Uncaught exceptions crash applications in production. Defensive exception handling makes services resilient against malformed user inputs, network dropouts, and resource constraints.

## Core Concepts
1. **`try`**: Encapsulates code that might raise an exception.
2. **`except ExceptionType`**: Catches specific errors safely without crashing.
3. **`else`**: Runs code that should only execute if the `try` block succeeded cleanly.
4. **`finally`**: Guarantees cleanup (e.g. closing database connections or open file handles).

## Syntax
```python
try:
    number = int("42")
    result = 100 / number
except ValueError as e:
    print(f"Invalid integer conversion: {e}")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print(f"Division succeeded: {result}")
finally:
    print("Execution pass complete.")
```

## Next Topic
Next: `17_basic_file_handling` — File I/O using `open()`, context managers (`with`), reading/writing, and `pathlib`.
