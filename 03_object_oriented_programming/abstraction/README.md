# Topic: Abstraction & Abstract Base Classes (`abc.ABC`)

## What You Will Learn
- Abstract Base Classes using `abc.ABC` module.
- Declaring mandatory interface contracts using `@abstractmethod`.
- Preventing instantiation of abstract classes directly (`TypeError`).
- Enforcing consistent API contracts across sub-components.

## Syntax
```python
from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self) -> None:
        pass

    @abstractmethod
    def query(self, sql: str) -> list:
        pass
```

## Next Topic
Next: `magic_methods` — Dunder methods (`__str__`, `__repr__`, `__len__`, `__getitem__`, operator overloading).
