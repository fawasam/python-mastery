# Topic 03: Scalar Data Types & Type Conversion

## What You Will Learn
- Python's core scalar (primitive) data types: `int`, `float`, `str`, `bool`, and `NoneType`.
- Checking types using the `type()` built-in function.
- Converting between data types (type casting): `int()`, `float()`, `str()`, `bool()`.
- Truthy vs Falsy values in Python.

## Why This Matters
Data types dictate what operations are valid on data (e.g., adding numbers vs concatenating strings). Understanding truthiness and conversion is critical for control flow and user input validation.

## Core Concepts
1. **`int`**: Arbitrary-precision integers (`-5`, `0`, `42`, `1_000_000`).
2. **`float`**: Double-precision floating-point numbers (`3.14159`, `-0.001`, `1.5e-3`).
3. **`str`**: Textual sequence of Unicode characters (`"hello"`, `'world'`).
4. **`bool`**: Truth values (`True`, `False`). Inherits from `int` (`True == 1`, `False == 0`).
5. **`NoneType`**: Represents the absence of a value (`None`).

## Truthy & Falsy Rules
In boolean contexts (e.g., `if` statements), Python evaluates objects to `True` or `False`.
**Falsy values in Python**:
- `False`
- `None`
- Numeric zeros: `0`, `0.0`, `0j`
- Empty sequences/collections: `""`, `[]`, `()`, `{}`, `set()`

Everything else is **Truthy**.

## Syntax
```python
age = int("25")          # Explicit conversion from str to int
ratio = float(3)         # Convert int to float (3.0)
text = str(100.5)        # Convert float to str ("100.5")
is_valid = bool("hello") # True because non-empty string is truthy
```

## Next Topic
Next: `04_input_output` — Interacting with users via terminal input and output formatting.
