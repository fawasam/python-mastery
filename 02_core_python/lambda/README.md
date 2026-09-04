# Topic: Lambda Functions & Key Sorting

## What You Will Learn
- Anonymous functions syntax: `lambda arguments: expression`.
- Differences between named functions (`def`) and inline `lambda` expressions.
- Using `lambda` as key functions in `sorted()`, `min()`, `max()`, and `.sort()`.
- Limitations of `lambda` (single expression body, no assignments, no multi-line logic).

## Syntax
```python
# Lambda definition
double = lambda x: x * 2

# Key function sorting
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
students_sorted_by_grade = sorted(students, key=lambda student: student[1], reverse=True)
```

## Next Topic
Next: `map_filter_reduce` — Functional primitives and lazy evaluation.
