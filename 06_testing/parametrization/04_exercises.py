"""
Parametrization Exercises.
"""


def calculate_tax(amount: float, rate: float) -> float:
    if amount < 0 or rate < 0:
        raise ValueError("Amount and rate must be >= 0")
    return round(amount * rate, 2)


# Exercise 1 (Medium): Parametrized runner for calculate_tax
def run_calculate_tax_tests(cases: list[tuple[float, float, float]]) -> None:
    raise NotImplementedError("Implement run_calculate_tax_tests")
