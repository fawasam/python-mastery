# Descriptors in Python

## What You Will Learn
* The Python Descriptor Protocol (`__get__`, `__set__`, `__delete__`, `__set_name__`).
* Differences between **Data Descriptors** and **Non-Data Descriptors**.
* How descriptors power `@property`, `@classmethod`, `@staticmethod`, and ORM attributes.
* How to manage instance attribute storage safely without shared state bugs.

## Why This Matters
Descriptors are the underlying mechanism behind many of Python's key features (like `@property` and methods themselves). Mastering descriptors gives you total control over attribute access, attribute validation, and ORM design, allowing you to write elegant, reusable class tools.

## Prerequisites
* Classes and objects (`03_object_oriented_programming/classes_objects`)
* Properties (`03_object_oriented_programming/properties`)
* Dunder methods (`03_object_oriented_programming/magic_methods`)

## Core Concepts

### 1. Descriptor Protocol
A object becomes a **descriptor** when it defines at least one of these magic methods:
- `__get__(self, instance, owner=None)`: Called when retrieving an attribute.
- `__set__(self, instance, value)`: Called when assigning an attribute.
- `__delete__(self, instance)`: Called when deleting an attribute.
- `__set_name__(self, owner, name)`: (Python 3.6+) Called automatically when the descriptor is assigned to a class attribute to register the field name.

### 2. Data vs. Non-Data Descriptors
- **Data Descriptor**: Implements `__set__` and/or `__delete__`. Takes precedence over instance dictionary lookup.
- **Non-Data Descriptor**: Implements only `__get__`. Instance attributes override non-data descriptors.

## Syntax
```python
class ValidatedString:
    def __set_name__(self, owner, name):
        self.private_name = f"_{name}"

    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        return getattr(instance, self.private_name, "")

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError("Value must be a string")
        setattr(instance, self.private_name, value)
```

## Common Mistakes
* **Storing instance state on `self` inside descriptor**: Descriptor instances live on the class object. Storing state in `self.value` shares data across ALL instances of the target class! Always store in `instance.__dict__` or use `__set_name__` to set private instance attributes.
* **Forgetting `instance is None` handling**: When accessed from the class (e.g. `MyClass.descriptor_field`), `instance` is `None`. `__get__` should usually return `self` in this case.

## Exercises
See `04_exercises.py` for practice tasks covering string validation, bounds checking, and lazy evaluation descriptors.
