# Topic: Decorators & Function Wrappers

## What You Will Learn
- What a decorator is in Python (a function that accepts another function as an argument, adds behavior, and returns a modified function).
- Syntactic sugar `@decorator_name`.
- Preserving function metadata (`__name__`, `__doc__`) using `@functools.wraps`.
- Decorators accepting arguments (decorator factories).
- Practical uses: execution timing, logging, authentication, and caching.

## Core Concepts
1. **Higher-Order Functions**: In Python, functions are first-class objects—they can be passed as parameters and returned from other functions.
2. **`functools.wraps`**: Essential decorator helper that copies docstrings and function metadata from original target to wrapper function.

## Syntax
```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Before function execution")
        result = func(*args, **kwargs)
        print("After function execution")
        return result
    return wrapper

@my_decorator
def greet(name: str):
    print(f"Hello, {name}!")
```

## Next Topic
Next: `context_managers` — The `with` statement, `__enter__`, `__exit__`, and `contextlib`.
