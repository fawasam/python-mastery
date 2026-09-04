# Topic: Magic Methods (Dunder Methods) & Operator Overloading

## What You Will Learn
- What double-underscore ("dunder") methods are in Python.
- String representations: `__str__()` (user friendly) vs `__repr__()` (developer unambiguous).
- Container methods: `__len__()`, `__getitem__()`, `__setitem__()`, `__contains__()`.
- Operator overloading: `__add__()`, `__eq__()`, `__lt__()`, `__bool__()`.

## Syntax
```python
class Vector:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self) -> str:
        return f"Vector(x={self.x}, y={self.y})"
```

## Next Topic
Next: `dataclasses` — Clean data containers with `@dataclass`, field defaults, and immutability (`frozen=True`).
