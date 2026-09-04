"""
Solutions for Parametrization Exercises.
"""


def calculate_tax(amount: float, rate: float) -> float:
    if amount < 0 or rate < 0:
        raise ValueError("Amount and rate must be >= 0")
    return round(amount * rate, 2)


def run_calculate_tax_tests(cases: list[tuple[float, float, float]]) -> None:
    for amount, rate, expected in cases:
        result = calculate_tax(amount, rate)
        assert result == expected, f"Failed for ({amount}, {rate}): Got {result}, expected {expected}"
        print(f"[PASS] Tax ({amount}, {rate}) == {expected}")


if __name__ == "__main__":
    test_cases = [
        (100.0, 0.05, 5.0),
        (250.50, 0.10, 25.05),
        (0.0, 0.15, 0.0),
    ]
    run_calculate_tax_tests(test_cases)
