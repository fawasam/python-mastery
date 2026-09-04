# Topic 02: Variables & Dynamic Typing in Python

## What You Will Learn
- What a variable is in Python (a reference to an object in memory).
- Snake_case variable naming conventions (PEP 8 standard).
- Python's dynamic typing behavior (variables don't have fixed types; objects do).
- Variable reassignment, multiple assignment, and garbage collection of unreferenced objects.

## Why This Matters
Variables are how programs remember and manipulate data. Understanding how Python handles variable references in memory prevents bugs when working with mutable data structures later.

## Core Concepts
1. **Variables as Labels/References**: In Python, a variable is not a bucket holding a value; it is a label tagged onto a value in memory.
2. **Dynamic Typing**: You do not declare variable types explicitly (e.g., no `int x = 5;`). Python infers the type from the assigned value.
3. **PEP 8 Naming Rules**:
   - Use `snake_case` for variables and functions (`user_age`, `total_price`).
   - Use `ALL_CAPS` for constants (`MAX_RETRIES = 3`).
   - Variable names cannot start with numbers and cannot be reserved Python keywords (`class`, `def`, `if`, etc.).

## Syntax
```python
# Store user details
user_name = "Alice"
user_age = 30
is_active_subscriber = True

# Multiple assignment
x, y, z = 10, 20, 30
```

## Examples
```python
# Constant convention
DATABASE_PORT = 5432

# Reassigning variable to a different data type
data = "Initial String"
data = 42  # Python permits type reassignment due to dynamic typing
```

## Common Mistakes
- Using reserved keywords (e.g., `class = "Math"`).
- Invalid names starting with digits (e.g., `1st_place = "Gold"`).
- Expecting constants to be enforced by compiler (Python constants are conventions only).

## Exercises
- Easy: Define 3 variables storing your favorite book title, page count, and read status.
- Medium: Swap the values of two variables without using a 3rd temporary variable.
- Hard: Demonstrate dynamic typing by reassigning a variable through 3 different data types and checking `id()` and `type()`.
- Real World: Build a configuration block for an application server.

## Next Topic
Next: `03_data_types` — Deep dive into Python's built-in scalar data types.
