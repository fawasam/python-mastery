# Abstract Syntax Trees (AST) and Code Analysis

## What You Will Learn
- Parsing Python source code into syntax trees using `ast.parse()`
- Traversal via `ast.NodeVisitor` and mutation via `ast.NodeTransformer`
- Generating modified Python source code using `ast.unparse()` (Python 3.9+)
- Building custom linters, code rewrite tools, and static analysis checkers

## Why This Matters
AST manipulation underlies static analysis tools like `ruff`, `mypy`, `black`, and Security Scanners (Bandit). Operating on the AST allows analyzing code structure without executing unsafe code.

## AST Processing Flow

```text
 Python Source Code → [ ast.parse() ] → AST Tree → [ ast.NodeVisitor ] → Analysis Report
                                             ↓
                                   [ ast.unparse() ] → Modified Code String
```

## Examples
See `01_basic.py` and `02_examples.py` for runnable code.

## Exercises
Complete exercises in `04_exercises.py` and check `05_solution.py`.

## Next Topic
Proceed to `../introspection/`.
