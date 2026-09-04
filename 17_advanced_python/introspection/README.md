# Python Reflection and Introspection

## What You Will Learn
- Dynamic object inspection using `dir()`, `getattr()`, `setattr()`, `hasattr()`
- Inspecting callables and signatures using `inspect.signature()`
- Extracting docstrings and parameter type hints at runtime
- Inspecting class inheritance resolution (MRO - Method Resolution Order)

## Why This Matters
Introspection allows programs to inspect object attributes, signatures, types, and docstrings dynamically at runtime. Frameworks (FastAPI, pytest, Pydantic) use introspection to auto-generate docs and validate route handler signatures.

## Core `inspect` Utilities
- `inspect.signature(func)`: Inspect parameters, defaults, and return annotations.
- `inspect.getsource(func)`: Retrieve raw source code of callable.
- `inspect.isclass()` / `inspect.isroutine()`: Type checking predicates.

## Examples
See `01_basic.py` and `02_examples.py` for runnable code.

## Exercises
Complete exercises in `04_exercises.py` and check `05_solution.py`.

## Next Topic
Proceed to `../python_c_api_concepts/`.
