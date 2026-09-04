"""
Common Mistakes in Pytest.
"""


# MISTAKE 1: Forgetting to place assert keyword
def mistake_missing_assert() -> None:
    # DANGER: Line evaluates 1 + 1 == 2, but without 'assert', result is ignored!
    # If expression becomes False (1 + 1 == 3), test still passes silently!
    1 + 1 == 3  # BUG! Test passes even though calculation is incorrect!


# GOOD PRACTICE: Always use assert keyword explicitly
def good_pytest_assertion() -> None:
    assert 1 + 1 == 2


if __name__ == "__main__":
    mistake_missing_assert()
    good_pytest_assertion()
    print("Pytest assertion checks completed.")
