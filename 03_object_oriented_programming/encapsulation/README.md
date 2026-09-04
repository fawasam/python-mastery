# Topic: Encapsulation & Access Modifiers

## What You Will Learn
- Public attributes (`name`): Accessible from anywhere.
- Protected attributes (`_name`): Convention indicating attribute is intended for internal or subclass use.
- Strongly Private attributes (`__name__`): Triggers Python's **Name Mangling** (`_ClassName__attribute`).
- Encapsulating state using getter and setter methods.

## Syntax
```python
class Account:
    def __init__(self, balance: float):
        self._protected = "internal"
        self.__balance = balance  # Name mangled to _Account__balance

    def get_balance(self) -> float:
        return self.__balance
```

## Next Topic
Next: `abstraction` — Abstract Base Classes (`abc.ABC`) and `@abstractmethod`.
