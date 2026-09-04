# Topic: Classes & Objects in Python

## What You Will Learn
- Class definition syntax using the `class` keyword.
- Instantiating object instances.
- Understanding `self` (reference to the current object instance).
- Instance attributes vs class attributes.

## Core Concepts
1. **Class**: A blueprint defining attributes and methods for objects.
2. **Object**: A concrete instance created from a class blueprint in memory.
3. **`self`**: The explicit first parameter in instance methods representing the instance calling the method.

## Syntax
```python
class BankAccount:
    bank_name = "Global Bank"  # Class attribute shared across all instances

    def __init__(self, owner: str, balance: float):
        self.owner = owner     # Instance attribute unique to each object
        self.balance = balance

    def deposit(self, amount: float) -> None:
        self.balance += amount
```

## Next Topic
Next: `constructors` — Initialization logic, `__init__`, and `__new__` object instantiation.
