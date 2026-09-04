"""
Common Mistakes in Test Parametrization.
"""


# MISTAKE: Stopping execution on first failure inside manual for-loops instead of distinct test parameters
def mistake_single_loop_failure() -> None:
    test_data = [(2, True), (3, True), (4, True)]  # (3, True) is invalid!

    for val, expected in test_data:
        # DANGER: If (3, True) fails, loop terminates and case (4, True) is NEVER evaluated or reported!
        assert (val % 2 == 0) == expected


if __name__ == "__main__":
    print("In Pytest @pytest.mark.parametrize, each tuple becomes a separate test run, preserving isolation!")
