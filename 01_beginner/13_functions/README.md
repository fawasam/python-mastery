# Topic 13: Functions, Parameters, *args & **kwargs

## What You Will Learn
- Function definition syntax using `def`, parameters, and docstrings.
- Return values and returning `None` implicitly.
- Default argument values and positional vs keyword arguments.
- Variable-length positional arguments (`*args` -> tuple).
- Variable-length keyword arguments (`**kwargs` -> dict).
- Type hints on functions (`def func(param: int) -> str:`).

## Why This Matters
Functions are the primary unit of code reuse, modularity, and encapsulation in Python software engineering. Understanding `*args` and `**kwargs` allows creating flexible interfaces, decorators, and API wrappers.

## Core Concepts
1. **Docstrings (PEP 257)**: Triple-quoted strings immediately inside functions that document parameters, return values, and exceptions.
2. **`*args`**: Collects excess positional arguments into a `tuple`.
3. **`**kwargs`**: Collects excess keyword arguments into a `dict`.
4. **Mutable Default Argument Trap**: Never use mutable objects (`[]`, `{}`) as default parameter values!

## Syntax
```python
def calculate_shipping(weight: float, express: bool = False, *extra_fees, **metadata) -> float:
    """
    Calculate shipping cost based on package weight.

    Args:
        weight: Package weight in kilograms.
        express: Whether express delivery is requested.
        *extra_fees: Additional fee floats to sum.
        **metadata: Arbitrary metadata key-value pairs.

    Returns:
        Calculated total shipping cost.
    """
    base_cost = weight * 5.0
    if express:
        base_cost += 15.0
    return base_cost + sum(extra_fees)
```

## Next Topic
Next: `14_scope` — Local, Enclosing, Global, Built-in scope (LEGB rule) and `global`/`nonlocal` keywords.
