# Clean Code Principles in Python

## What You Will Learn
- Core clean code principles: DRY (Don't Repeat Yourself), KISS (Keep It Simple, Stupid), YAGNI (You Aren't Gonna Need It)
- Meaningful variable, function, and class naming conventions
- Function design: Small, single-purpose functions with few arguments
- Commenting philosophy: Explain *why*, not *what*

## Why This Matters
Code is read far more often than it is written. Writing clean code reduces technical debt, improves maintainability, simplifies debugging, and allows teams to scale development speed over time.

## Prerequisites
- Core Python syntax, functions, and data structures
- Type hints and docstrings

## Core Concepts

### 1. DRY (Don't Repeat Yourself)
Avoid duplicating logic. If the same logic appears in multiple places, extract it into a reusable function or class.

### 2. KISS (Keep It Simple, Stupid)
Avoid over-engineering. Choose simple, readable solutions over clever, obscure tricks.

### 3. YAGNI (You Aren't Gonna Need It)
Do not build features or abstractions until they are actually required.

### 4. Single Responsibility Principle (Functions)
A function should do one thing, do it well, and do it only.

## Examples
See `01_basic.py` and `02_examples.py` for comparative examples of dirty vs clean Python code.

## Common Mistakes
- Using non-descriptive variable names (`x`, `tmp`, `data1`).
- Functions taking 5+ parameters instead of grouping related parameters into data structures or classes.
- Deeply nested conditional blocks (pyramid of doom) instead of early returns (guard clauses).

## Best Practices
- Use guard clauses to exit early and reduce indentation levels.
- Limit functions to 20-30 lines of code.
- Prefer self-documenting code over excessive obvious comments.

## Exercises
Complete exercises in `04_exercises.py` and review solutions in `05_solution.py`.

## Next Topic
Proceed to `../solid/` to learn SOLID principles.
