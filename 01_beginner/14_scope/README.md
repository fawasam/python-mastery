# Topic 14: Variable Scope & The LEGB Rule

## What You Will Learn
- Understanding variable resolution order in Python: **LEGB Rule**.
  - **L**ocal: Inside the current function block.
  - **E**nclosing: Inside nested outer function blocks.
  - **G**lobal: Module-level scope.
  - **B**uilt-in: Python reserved built-ins (`print`, `len`, `int`).
- Modifying outer variables using the `global` keyword.
- Modifying enclosing nested variables using the `nonlocal` keyword.

## Why This Matters
Scope rules govern variable visibility and lifetime. Misunderstanding scope causes `UnboundLocalError`, accidental shadowing of global states, and broken state retention in closures.

## Core Concepts
1. **LEGB Lookup**: When referencing a variable name `x`, Python searches sequentially in Local -> Enclosing -> Global -> Built-in. The first match found is used.
2. **`global x`**: Declares that `x` inside a function refers to the module-level global variable.
3. **`nonlocal x`**: Declares that `x` refers to the variable in the nearest enclosing non-global scope (used in nested functions & closures).

## Syntax
```python
counter = 0  # Global scope

def increment_global():
    global counter
    counter += 1

def outer():
    count = 0  # Enclosing scope
    def inner():
        nonlocal count
        count += 1
    inner()
```

## Next Topic
Next: `15_modules` — Module imports, aliasing, `__name__ == "__main__"`, and standard library utilities.
