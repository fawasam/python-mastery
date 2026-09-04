# Topic: Dataclasses & Modern Data Containers

## What You Will Learn
- `@dataclass` decorator (PEP 557).
- Automatic generation of `__init__`, `__repr__`, `__eq__`.
- Field defaults and `field(default_factory=...)` for mutable default attributes.
- Immutable dataclasses (`frozen=True`).
- Post-initialization validation logic using `__post_init__()`.

## Syntax
```python
from dataclasses import dataclass, field

@dataclass(frozen=True)
class UserDTO:
    id: int
    name: str
    roles: list[str] = field(default_factory=list)
```

## Next Topic
Next: `properties` — Encapsulating attributes with `@property`, `@setter`, and `@deleter`.
