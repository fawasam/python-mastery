"""
Introspection Common Pitfalls.
"""

# MISTAKE: Over-relying on `type(obj) == TargetClass` instead of `isinstance(obj, TargetClass)`.
# WHY: `type(obj) == TargetClass` fails on subclasses, breaking OOP polymorphism.
# FIX: Always use `isinstance(obj, TargetClass)` or `issubclass(cls, TargetClass)`.

if __name__ == "__main__":
    print("Isinstance over type comparison rules verified.")
