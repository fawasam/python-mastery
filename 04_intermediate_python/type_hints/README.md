# Topic: Modern Type Hints (PEP 484 & PEP 604)

## What You Will Learn
- Variable annotations, function parameter annotations, and return type annotations.
- Python 3.10+ modern union syntax `int | float` (replacing `Union[int, float]`).
- Python 3.10+ nullable syntax `str | None` (replacing `Optional[str]`).
- Static type checking with `mypy`.

## Syntax
```python
def process_score(val: int | float) -> str:
    return f"Score: {val:.1f}"

user_email: str | None = None
```

## Next Topic
Next: `typing` — `Callable`, `Generic`, `TypeVar`, `Any`, and `Literal`.
