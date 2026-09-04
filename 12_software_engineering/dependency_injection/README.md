# Dependency Injection in Python

## What You Will Learn
- What Dependency Injection (DI) is and why it decoupling components
- Constructor Injection vs Property Injection vs Function Parameter Injection
- Building simple DI containers and using DI frameworks (FastAPI Depends)

## Why This Matters
Hardcoding object construction inside dependent classes binds components tightly together. Dependency Injection provides objects with their required dependencies from the outside, enabling painless unit testing (using mocks/fakes) and modular component swapping.

## Prerequisites
- SOLID Principles (specifically Dependency Inversion Principle)
- Object-Oriented Programming & Typing Protocols

## Core Concepts

### Types of Dependency Injection
1. **Constructor Injection**: Passing dependencies into `__init__()` (Most common and recommended).
2. **Function Parameter Injection**: Passing dependencies as arguments to specific functions (e.g. FastAPI route handlers).
3. **Property / Setter Injection**: Injecting dependencies after object instantiation via property setters.

## Examples
See `01_basic.py` (Constructor & Function DI) and `02_examples.py` (Mini Container).

## Exercises
Complete exercises in `04_exercises.py` and verify solutions in `05_solution.py`.

## Next Topic
Proceed to `../architecture/`.
