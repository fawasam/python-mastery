"""
Solutions for Pytest Exercises.
"""


def sanitize_username(raw: str) -> str:
    cleaned = raw.strip().lower()
    if not cleaned:
        raise ValueError("Username cannot be empty")
    return cleaned


def test_sanitize_username_valid() -> None:
    assert sanitize_username("  AliceSmith  ") == "alicesmith"


def test_sanitize_username_empty() -> None:
    try:
        sanitize_username("   ")
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert "cannot be empty" in str(e)


if __name__ == "__main__":
    test_sanitize_username_valid()
    test_sanitize_username_empty()
    print("Pytest exercise solutions passed.")
