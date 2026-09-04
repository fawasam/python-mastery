# Topic 08: Loops, Iteration & Control Directives

## What You Will Learn
- `for` loops: Iterating over sequences (`range()`, `list`, `str`, `tuple`).
- `while` loops: Executing code while a condition remains `True`.
- Loop control statements: `break` (exit loop), `continue` (skip iteration), `pass` (placeholder).
- `else` clause attached to loops: Executes ONLY if the loop completes naturally without hitting a `break`.

## Why This Matters
Iteration is essential for automation, batch data processing, searching datasets, and polling system states. Understanding `for-else` and `while-else` prevents redundant boolean flags when searching.

## Core Concepts
1. **`range(start, stop, step)`**: Generates an immutable sequence of numbers on demand (lazy evaluation).
2. **`break`**: Immediately terminates the innermost enclosing loop.
3. **`continue`**: Skips the remainder of the current loop iteration and moves to the next pass.
4. **`loop-else`**:
   ```python
   for item in items:
       if item == target:
           print("Found target!")
           break
   else:
       print("Target was not found in items!")  # Triggers if loop finishes without break
   ```

## Next Topic
Next: `09_lists` — Indexing, mutability, appending, popping, sorting, and list operations.
