# Topic: Advanced `typing` Module Constructs

## What You Will Learn
- `Callable[[ArgTypes], ReturnType]`.
- Generics with `TypeVar` and `Generic[T]`.
- Fixed options with `Literal["READ", "WRITE"]`.
- Flexible typing with `Any` vs `object`.

## Syntax
```python
from typing import Callable, Generic, Literal, TypeVar

T = TypeVar("T")

class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()

Mode = Literal["read", "write"]
```

## Next Topic
Next: `protocols` — Structural subtyping (PEP 544).
