# Topic 05: Operators in Python

## What You Will Learn
- Arithmetic operators: `+`, `-`, `*`, `/`, `//` (floor division), `%` (modulus), `**` (exponentiation).
- Comparison operators: `==`, `!=`, `>`, `<`, `>=`, `<=`.
- Logical operators: `and`, `or`, `not` (short-circuit evaluation).
- Assignment operators: `=`, `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`.
- Identity operators (`is`, `is not`) vs Equality operators (`==`, `!=`).
- Membership operators (`in`, `not in`).

## Why This Matters
Operators form the computational backbone of algorithm logic, conditional statements, and mathematical calculations. Understanding identity (`is`) vs equality (`==`) avoids severe bugs when comparing objects in Python.

## Core Concepts
1. **Floor Division (`//`)**: Divides and rounds down to nearest integer (`7 // 2 -> 3`).
2. **Modulus (`%`)**: Returns remainder of division (`7 % 2 -> 1`). Useful for checking even/odd numbers and cyclic indexing.
3. **Short-Circuit Evaluation**:
   - `A and B`: If `A` is falsy, `B` is never evaluated.
   - `A or B`: If `A` is truthy, `B` is never evaluated.
4. **`==` vs `is`**:
   - `==`: Checks if values are equal.
   - `is`: Checks if objects point to the exact same memory address.

## Syntax
```python
is_even = (number % 2 == 0)
has_access = (is_admin or is_owner) and not is_suspended
in_allowed_list = user_role in ["admin", "editor", "author"]
```

## Next Topic
Next: `06_strings` — String indexing, slicing, methods, immutability, and operations.
