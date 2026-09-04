# Advanced Context Managers and Contextlib Utilities

## What You Will Learn
- Class-based context managers (`__enter__` and `__exit__`)
- Generator-based context managers using `@contextlib.contextmanager`
- Reentrant context managers (`contextlib.redirect_stdout`, `ExitStack`)
- Handling exceptions inside `__exit__` (returning `True` to suppress errors)

## Why This Matters
Context managers guarantee resource cleanup (closing DB connections, unlocking mutexes, removing temp files) regardless of whether code block execution succeeds or raises an exception.

## Examples
See `01_basic.py` and `02_examples.py` for runnable code.

## Exercises
Complete exercises in `04_exercises.py` and check `05_solution.py`.

## Next Topic
Proceed to `../bytecode/`.
