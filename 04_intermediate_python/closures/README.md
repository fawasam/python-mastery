# Closures in Python

## What You Will Learn
* What a closure is and how lexical scoping works in Python.
* The `nonlocal` keyword and when to use it.
* Inspecting free variables via `func.__closure__`.
* Stateful functions without using classes.

## Why This Matters
Closures are the foundational building block for decorators, event handlers, function factories, and functional programming paradigms. Understanding how inner functions "remember" variables from outer scopes is vital for advanced Python architecture.

## Prerequisites
* Functions and Scope (`01_beginner/13_functions`, `01_beginner/14_scope`)

## Core Concepts

### What is a Closure?
A closure is an inner function that retains access to variables from its enclosing scope (lexical scope) even after the outer function has finished executing.

To form a closure in Python:
1. There must be a nested function (a function inside a function).
2. The nested function must refer to a variable defined in the enclosing scope.
3. The outer function must return the nested function.

## Syntax
```python
def make_counter(start: int = 0):
    count = start

    def counter() -> int:
        nonlocal count  # Allows mutating the outer variable 'count'
        count += 1
        return count

    return counter
```

## Common Mistakes
* **Missing `nonlocal`**: Trying to reassign an outer variable inside an inner function creates a local variable instead of mutating the outer one, leading to `UnboundLocalError`.
* **Late Binding in Loops**: Creating closures in loops where all inner functions capture the same variable reference, evaluating its final loop value.

## Exercises
See `04_exercises.py` for practice creating stateful function factories and rate-limiting helper functions.
