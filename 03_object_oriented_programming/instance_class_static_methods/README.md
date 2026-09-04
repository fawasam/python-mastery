# Topic: Instance Methods, `@classmethod` & `@staticmethod`

## What You Will Learn
- Instance Methods (`self`): Operate on individual instance attributes.
- Class Methods (`@classmethod`, `cls`): Operate on class-level attributes and serve as factory constructors.
- Static Methods (`@staticmethod`): Utility functions scoped inside a class that do not reference `self` or `cls`.

## Core Concepts
| Method Type | Decorator | First Arg | Usage |
|---|---|---|---|
| Instance Method | None | `self` | Read/modify object state |
| Class Method | `@classmethod` | `cls` | Read/modify class state or create instances |
| Static Method | `@staticmethod` | None | Pure utility helper functions |

## Next Topic
Next: `inheritance` — Single inheritance, multiple inheritance, `super()`, and Method Resolution Order (MRO).
