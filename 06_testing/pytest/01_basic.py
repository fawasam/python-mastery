"""
Basic Pytest Example.
"""


def format_user_name(first: str, last: str) -> str:
    if not first or not last:
        raise ValueError("First and last name required")
    return f"{last.upper()}, {first.title()}"


def test_format_user_name_valid() -> None:
    # Pytest automatically inspects standard Python 'assert' expressions!
    result = format_user_name("john", "doe")
    assert result == "DOE, John"


def test_format_user_name_empty_raises_error() -> None:
    try:
        format_user_name("", "doe")
        assert False, "Expected ValueError was not raised"
    except ValueError as e:
        assert "required" in str(e)


if __name__ == "__main__":
    test_format_user_name_valid()
    test_format_user_name_empty_raises_error()
    print("All basic pytest assertion tests passed successfully!")
