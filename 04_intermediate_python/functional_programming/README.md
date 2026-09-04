# Topic: Functional Programming in Python (`functools.partial`, Pure Functions)

## What You Will Learn
- Pure functions (no side-effects, deterministic return values).
- Immutability concepts.
- Partial function application using `functools.partial`.
- Currying and function composition.

## Syntax
```python
from functools import partial

def multiply(a: int, b: int) -> int:
    return a * b

double = partial(multiply, 2)
print(double(5)) # 10
```

## Next Topic
Next: `descriptors` — Attribute access customization with `__get__`, `__set__`, `__delete__`.
