# Topic: Constructors & Object Instantiation (`__init__` and `__new__`)

## What You Will Learn
- Instance initialization with `__init__()`.
- Object creation mechanics with `__new__()` (the actual constructor method).
- Using `@classmethod` for alternative factory constructors (e.g. `User.from_json()`, `User.from_dict()`).

## Syntax
```python
class User:
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data["username"], data["email"])
```

## Next Topic
Next: `instance_class_static_methods` — `@classmethod` vs `@staticmethod` vs Instance methods.
