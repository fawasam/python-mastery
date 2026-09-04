# Python Code Refactoring Techniques

## What You Will Learn
- What code refactoring is (altering code internal structure without changing external behavior)
- Identifying code smells (Long Method, Feature Envy, Primitive Obsession, Large Class)
- Step-by-step refactoring strategies: Extract Method, Replace Conditional with Polymorphism, Introduce Parameter Object
- Refactoring safely using automated tests as a safety net

## Why This Matters
As software evolves over time, quick fixes introduce technical debt. Refactoring cleans up bad design, improves code clarity, and keeps development velocity high without changing application behavior.

## Common Code Smells & Refactorings

| Code Smell | Description | Refactoring Technique |
|---|---|---|
| **Long Method** | Function contains 50+ lines doing multiple things | Extract Method |
| **Primitive Obsession** | Using raw strings/tuples instead of small objects | Replace Primitive with Object / Dataclass |
| **Complex Conditional** | Deeply nested `if/elif/else` statements | Replace Conditional with Polymorphism or Guard Clauses |
| **Feature Envy** | Method uses another class's data more than its own | Move Method |

## Examples
See `01_basic.py` (Extract Method & Parameter Object) and `02_examples.py` (Replacing Conditionals with Polymorphism).

## Exercises
Complete exercises in `04_exercises.py` and check solutions in `05_solution.py`.

## Next Topic
Complete the Software Engineering Mini Project in `../mini_project/`.
