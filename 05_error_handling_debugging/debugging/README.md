# Debugging Python Applications

## What You Will Learn
* Interactive debugging with Python's built-in `breakpoint()` / `pdb` module.
* Key `pdb` commands (`n`, `s`, `c`, `p`, `pp`, `l`, `w`, `q`).
* Inspecting local stack frames and tracebacks (`traceback` module).
* Post-mortem debugging of unhandled exceptions.

## Why This Matters
Relying solely on `print()` for debugging complex systems is slow and inefficient. Using `breakpoint()` allows you to pause execution dynamically, inspect variable states live, step through lines of code, and pinpoint the exact source of unexpected state mutations.

## Prerequisites
* Functions & Scope (`01_beginner/14_scope`)
* Exceptions (`05_error_handling_debugging/exceptions`)

## Core Concepts

### 1. `breakpoint()` Statement
Introduced in Python 3.7, `breakpoint()` drops you into an interactive debugger shell (`pdb`) right at the line where it is invoked.

### 2. Common `pdb` Commands
- `n` (next): Execute current line and advance to the next line in current function.
- `s` (step): Execute current line and step *into* any function call.
- `c` (continue): Resume normal execution until next breakpoint or program termination.
- `p variable` (print): Evaluate and print the variable value.
- `pp variable` (pretty print): Formatted print of complex dicts/lists.
- `l` (list): Show source code around current frame.
- `q` (quit): Abort debugger and program.

## Syntax
```python
def process_user_data(user_dict: dict) -> float:
    age = user_dict.get("age", 0)
    multiplier = 1.5
    # Pause execution here to inspect local scope
    breakpoint()
    return age * multiplier
```

## Exercises
See `04_exercises.py` to practice fixing tracebacks and step-debugging algorithms.
