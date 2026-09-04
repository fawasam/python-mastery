"""
Basic Parametrized Testing Pattern.
"""


def is_even(n: int) -> bool:
    return n % 2 == 0


def run_parametrized_test_cases(test_cases: list[tuple[int, bool]]) -> None:
    for n, expected in test_cases:
        assert is_even(n) == expected, f"Failed for input {n}: expected {expected}"
        print(f"[PASS] is_even({n}) == {expected}")


if __name__ == "__main__":
    cases = [
        (2, True),
        (3, False),
        (0, True),
        (-4, True),
        (-7, False),
    ]
    run_parametrized_test_cases(cases)
