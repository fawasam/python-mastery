"""
Solutions for Assertion Exercises.
"""


def assert_all_positive(numbers: list[int]) -> None:
    assert len(numbers) > 0, "List cannot be empty"
    assert all(x > 0 for x in numbers), "All numbers must be strictly positive"


if __name__ == "__main__":
    assert_all_positive([1, 2, 3])
    print("Assertion passed for [1, 2, 3]")

    try:
        assert_all_positive([1, -5, 3])
    except AssertionError as e:
        print(f"Assertion caught correctly: {e}")
