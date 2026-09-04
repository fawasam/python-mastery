"""
Basic Assertions in Python.
"""


def calculate_average(scores: list[float]) -> float:
    # Internal invariant assertion check: input list must not be empty
    assert len(scores) > 0, "Scores list must not be empty"

    total = sum(scores)
    avg = total / len(scores)

    # Output invariant check
    assert 0.0 <= avg <= 100.0, f"Average {avg} out of range [0, 100]"

    return avg


if __name__ == "__main__":
    valid_scores = [85.0, 90.0, 95.0]
    print(f"Average: {calculate_average(valid_scores)}")

    try:
        calculate_average([])
    except AssertionError as err:
        print(f"Assertion Caught: {err}")
