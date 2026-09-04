# Software Design Patterns in Python

## What You Will Learn
- Creational Patterns: Factory Method, Singleton, Builder
- Structural Patterns: Adapter, Decorator, Facade
- Behavioral Patterns: Strategy, Observer, Command

## Why This Matters
Design patterns provide standard, proven templates for solving recurring software design problems. Using well-known patterns establishes a common vocabulary for team developers and leads to clean, decoupled object structures.

## Prerequisites
- Object-Oriented Programming (Classes, Inheritance, Interfaces)
- SOLID Principles

## Classification of Patterns

### 1. Creational Patterns
Focus on object creation mechanisms.
- **Factory Method**: Interface for creating objects in a superclass, letting subclasses alter the object type created.
- **Singleton**: Ensures a class has only one instance while providing a global access point.

### 2. Structural Patterns
Focus on how classes and objects are composed to form larger structures.
- **Adapter**: Allows objects with incompatible interfaces to collaborate.
- **Facade**: Provides a simplified interface to a complex library or framework.

### 3. Behavioral Patterns
Focus on algorithms and assignment of responsibilities between objects.
- **Strategy**: Defines a family of algorithms, puts each in a separate class, and makes their objects interchangeable.
- **Observer**: Defines a subscription mechanism to notify multiple objects about events.

## Examples
See `01_basic.py` (Factory & Strategy) and `02_examples.py` (Observer & Adapter).

## Exercises
Complete exercises in `04_exercises.py` and verify in `05_solution.py`.

## Next Topic
Proceed to `../dependency_injection/`.
