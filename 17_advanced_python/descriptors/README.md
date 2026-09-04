# Attribute Access Customization via Descriptors

## What You Will Learn
- What Python Descriptors are (`__get__`, `__set__`, `__delete__`)
- Data descriptors vs Non-data descriptors
- Using `__set_name__` (Python 3.6+) for automatic attribute naming
- Building reusable type-checking and validation descriptors

## Why This Matters
Descriptors underlie Python's fundamental features: `@property`, `@classmethod`, `@staticmethod`, ORM fields (SQLAlchemy/Django), and Pydantic field validators.

## Descriptor Protocol
```python
class Descriptor:
    def __set_name__(self, owner, name):
        self.private_name = f"_{name}"

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.private_name, None)

    def __set__(self, instance, value):
        setattr(instance, self.private_name, value)
```

## Examples
See `01_basic.py` and `02_examples.py` for runnable code.

## Exercises
Complete exercises in `04_exercises.py` and check `05_solution.py`.

## Next Topic
Proceed to `../decorators/`.
