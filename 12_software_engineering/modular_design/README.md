# Modular Design and Package Organization in Python

## What You Will Learn
- Structuring Python modules and packages using `__init__.py`
- Explicit exports using `__all__`
- Low coupling and high cohesion design goals
- Circular import prevention strategies

## Why This Matters
As Python applications grow beyond a few files, unstructured imports and tight coupling lead to circular import errors, brittle dependencies, and nightmare refactoring. Proper modularization divides system features into cohesive, self-contained packages.

## Core Concepts

### 1. High Cohesion
Elements within a single module should belong together and serve a unified, clear function.

### 2. Low Coupling
Modules should depend on each other as little as possible, interacting primarily through well-defined interfaces/contracts.

### 3. Exposing Public API (`__all__`)
Control what symbols are exported when consumers run `from package import *`.

```python
# __init__.py
__all__ = ["PublicService", "PublicModel"]
```

## Examples
See `01_basic.py` (Package exports & `__all__`) and `02_examples.py` (Decoupled plugin architecture).

## Exercises
Complete exercises in `04_exercises.py` and verify solutions in `05_solution.py`.

## Next Topic
Proceed to `../refactoring/`.
