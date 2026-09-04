# Topic 07: Conditionals & Control Flow

## What You Will Learn
- Branching logic using `if`, `elif`, and `else`.
- Indentation blocks in Python (4 spaces PEP 8 standard).
- Nested conditional blocks and avoiding deep nesting antipatterns (arrow code).
- Single-line conditional expressions (ternary operator: `value_if_true if condition else value_if_false`).

## Why This Matters
Conditionals enable dynamic execution paths based on runtime state, user inputs, feature flags, and business validation rules.

## Core Concepts
1. **Indentation**: Python uses indentation instead of curly braces `{}` to define scope blocks.
2. **`elif` Short for Else If**: Evaluates sequentially until the first `True` condition is encountered; remaining blocks are skipped.
3. **Ternary Operator**: Compact expression for assigning values conditionally:
   `status = "Adult" if age >= 18 else "Minor"`
4. **Guard Clauses**: Returning early from functions to eliminate deep nesting.

## Syntax
```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"
```

## Next Topic
Next: `08_loops` — Iterating with `for` and `while` loops, `break`, `continue`, `pass`, and `else` blocks with loops.
