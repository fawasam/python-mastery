# Topic: Inheritance, `super()` & MRO

## What You Will Learn
- Class inheritance syntax: `class SubClass(SuperClass):`.
- Calling parent methods and initializer using `super().__init__()`.
- Method Overriding (customizing parent class behavior in derived classes).
- Multiple inheritance and Method Resolution Order (`Class.mro()`).

## Syntax
```python
class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        return "Generic animal sound"

class Dog(Animal):
    def speak(self) -> str:
        return f"{self.name} barks: Woof!"
```

## Next Topic
Next: `polymorphism` — Duck typing and polymorphic interface behavior.
