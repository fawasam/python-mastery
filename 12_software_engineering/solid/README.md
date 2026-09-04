# SOLID Design Principles in Python

## What You Will Learn
- **S**: Single Responsibility Principle (SRP)
- **O**: Open/Closed Principle (OCP)
- **L**: Liskov Substitution Principle (LSP)
- **I**: Interface Segregation Principle (ISP)
- **D**: Dependency Inversion Principle (DIP)

## Why This Matters
The SOLID principles are foundational software architecture rules. Designing code around SOLID ensures object-oriented applications remain scalable, easy to test, and adaptable to changing business requirements without regression bugs.

## Prerequisites
- Object-Oriented Programming (Classes, Inheritance, Abstract Base Classes)
- Type Hints and Protocols

## Core Principles

1. **SRP (Single Responsibility)**: A class should have one, and only one, reason to change.
2. **OCP (Open/Closed)**: Software entities should be open for extension, but closed for modification.
3. **LSP (Liskov Substitution)**: Subtypes must be substitutable for their base types without altering program correctness.
4. **ISP (Interface Segregation)**: Clients should not be forced to depend upon interfaces they do not use.
5. **DIP (Dependency Inversion)**: High-level modules should not depend on low-level modules; both should depend on abstractions.

## Examples
See `01_basic.py` for SRP, OCP, LSP examples, and `02_examples.py` for ISP and DIP examples.

## Common Mistakes
- Violating OCP by using large `if/elif/else` chains over object types instead of polymorphism.
- Violating LSP by having subclasses throw `NotImplementedError` or change method signatures.
- Violating DIP by directly instantiating low-level dependencies inside high-level service classes.

## Best Practices
- Depend on Abstract Base Classes (ABCs) or Protocols rather than concrete implementations.
- Prefer composition and interfaces over deep inheritance trees.

## Exercises
See `04_exercises.py` and solutions in `05_solution.py`.

## Next Topic
Proceed to `../design_patterns/`.
