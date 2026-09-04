# Metaclasses and Class Construction Internals

## What You Will Learn
- What a metaclass is in Python ("a class of a class")
- `type` as the default metaclass of all objects
- Custom class creation using `__new__` vs class initialization using `__init__`
- `__init_subclass__` as a modern, simpler alternative to metaclasses

## Why This Matters
Metaclasses control class creation itself. Frameworks like Django ORM, Pydantic, and SQLAlchemy use metaclasses to intercept class definition, register fields, enforce naming rules, and generate database schemas automatically.

## Core Metaclass Mechanics
```python
class Meta(type):
    def __new__(cls, name, bases, dct):
        # Modify class dictionary dct before class creation
        return super().__new__(cls, name, bases, dct)
```

## Examples
See `01_basic.py` and `02_examples.py` for runnable code.

## Exercises
Complete exercises in `04_exercises.py` and check `05_solution.py`.

## Next Topic
Proceed to `../descriptors/`.
