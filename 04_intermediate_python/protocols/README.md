# Topic: Structural Subtyping & Protocols (PEP 544)

## What You Will Learn
- Protocols as static duck typing interfaces (`typing.Protocol`).
- Static type verification without explicit inheritance hierarchy.
- `@runtime_checkable` decorator enabling `isinstance()` checks on protocols.

## Syntax
```python
from typing import Protocol, runtime_checkable

@runtime_checkable
class Renderable(Protocol):
    def render(self) -> str:
        ...
```

## Next Topic
Next: `abstract_base_classes` — Nominal subtyping contracts using `abc.ABC`.
