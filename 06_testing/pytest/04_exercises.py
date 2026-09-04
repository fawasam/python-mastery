"""
Pytest Exercises.
"""


def sanitize_username(raw: str) -> str:
    cleaned = raw.strip().lower()
    if not cleaned:
        raise ValueError("Username cannot be empty")
    return cleaned


# Exercise 1 (Easy): Write pytest functions for sanitize_username
def test_sanitize_username_valid() -> None:
    raise NotImplementedError("Implement test_sanitize_username_valid")


def test_sanitize_username_empty() -> None:
    raise NotImplementedError("Implement test_sanitize_username_empty")
