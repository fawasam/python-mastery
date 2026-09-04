"""
Metaclass Common Pitfalls.
"""

# MISTAKE: Re-inventing custom Metaclasses when `__init_subclass__` or Class Decorators would suffice.
# WHY: Metaclasses introduce complex inheritance hierarchy conflicts (metaclass conflicts).
# FIX: Prefer `__init_subclass__` or class decorators unless intercepting class creation itself is strictly required.

if __name__ == "__main__":
    print("Metaclass over-engineering avoidance rules verified.")
