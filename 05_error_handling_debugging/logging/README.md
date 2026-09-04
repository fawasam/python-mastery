# Logging in Python

## What You Learn
* Python's standard `logging` library.
* Log levels (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`).
* `logging.basicConfig()` vs configuring modular `getLogger(__name__)`.
* Log Formatting, Handlers (`StreamHandler`, `FileHandler`), and Formatters.
* Exception stack trace logging with `logger.exception()` / `exc_info=True`.

## Why This Matters
`print()` statements are ephemeral and pollute stdout. The standard `logging` framework allows you to output structured logs to files, stdout, or remote monitoring services with configurable severity filters and formatting without changing source code.

## Prerequisites
* Basic I/O (`01_beginner/04_input_output`)

## Core Concepts

### 1. Log Levels
- `DEBUG` (10): Detailed diagnostic output for development.
- `INFO` (20): Normal operational events.
- `WARNING` (30): Unexpected events or potential issues.
- `ERROR` (40): Errors preventing a specific function from executing.
- `CRITICAL` (50): Severe failures causing program shutdown.

### 2. Recommended Logging Pattern
Always instantiate module-level loggers with `logging.getLogger(__name__)`:

```python
import logging

logger = logging.getLogger(__name__)

def process_payment(amount: float) -> None:
    logger.info("Processing payment of $%.2f", amount)
    try:
        ...
    except Exception:
        logger.exception("Payment processing failed")
```

## Common Mistakes
* **Using `print()` instead of `logging`**: Cannot be filtered, muted, or routed in production environments.
* **Using string formatting `%` or `f""` inside log calls directly**: `logger.info(f"User {name}")` formats strings even if INFO log level is currently disabled! Pass arguments as extra args: `logger.info("User %s", name)`.

## Exercises
See `04_exercises.py` to practice creating dual file/console logger configurations.
