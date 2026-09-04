# Topic 04: Input & Output in Python

## What You Will Learn
- Reading user input from standard input using `input()`.
- Understanding that `input()` ALWAYS returns a string.
- Advanced string formatting using f-strings (PEP 498), `str.format()`, and `%` formatting.
- Formatting floating point numbers, alignment, padding, and thousand separators in f-strings.

## Why This Matters
Interactive CLI programs rely on `input()` to receive commands and configuration from users. Formatting output cleanly makes command-line tools user-friendly and professional.

## Core Concepts
1. **`input(prompt)`**: Pauses execution, prints optional `prompt`, reads a line from stdin, and returns it as `str`.
2. **Type Casting Input**: Because `input()` returns `str`, numeric inputs must be explicitly cast using `int(input())` or `float(input())`.
3. **f-string Precision Specifiers**:
   - `{val:.2f}`: Round float to 2 decimal places.
   - `{val:,}`: Add commas as thousand separators (`1,000,000`).
   - `{val:>10}`: Right-align in a field of width 10.
   - `{val:<10}`: Left-align in a field of width 10.
   - `{val:^10}`: Center-align in a field of width 10.

## Syntax
```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
price = 1234.5678

print(f"User {name} ({age}) logged in.")
print(f"Formatted price: ${price:,.2f}") # Output: $1,234.57
```

## Next Topic
Next: `05_operators` — Arithmetic, logical, comparison, assignment, bitwise, and membership operators.
