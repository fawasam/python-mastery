# Topic: Composition vs Inheritance ("Has-A" Relationships)

## What You Will Learn
- The design rule: *"Favor composition over inheritance."*
- Difference between "Is-A" (Inheritance) and "Has-A" (Composition) relationships.
- Delegating behavior to specialized component objects.
- Building flexible, loosely coupled system architectures.

## Syntax
```python
class Engine:
    def start(self): return "Vroom!"

class Car:
    def __init__(self, engine: Engine):
        self.engine = engine  # Car HAS AN Engine (Composition)

    def start(self):
        return self.engine.start()
```

## Next Topic
Next: Section 3 Mini-Project — Building an Object-Oriented Library Management System!
