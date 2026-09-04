# Topic: Generators, `yield` & Generator Expressions

## What You Will Learn
- What a generator is (a special function that yields values lazily one-at-a-time).
- The `yield` keyword vs `return` keyword.
- Generator expressions: `(expr for item in iterable)`.
- Memory profiling: processing gigabyte-scale streams in constant `O(1)` memory.
- Generator pipelines: chaining generator functions together.

## Syntax
```python
# Generator Function
def count_up_to(max_val: int):
    n = 1
    while n <= max_val:
        yield n
        n += 1

# Generator Expression
squares = (x**2 for x in range(1_000_000))
```

## Next Topic
Next: `decorators` — Function wrappers, `@wraps`, and stateful decorators.
