"""
Defensive Programming Exercises.
"""


# Exercise 1 (Medium): Refactoring Nested Code to Guard Clauses
# Refactor calculate_shipping_cost to use guard clauses and fail fast.
# Preconditions:
# - weight must be > 0 (raise ValueError if <= 0)
# - distance must be > 0 (raise ValueError if <= 0)
# - destination_country must be a non-empty string (raise ValueError if empty)
def calculate_shipping_cost(weight: float, distance: float, destination_country: str) -> float:
    raise NotImplementedError("Implement calculate_shipping_cost using guard clauses")
