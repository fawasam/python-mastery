"""
Basic TDD Workflow Demonstration: Password Strength Validator.
"""


# STEP 1 & 2: Production function developed iteratively via TDD
def is_password_strong(password: str) -> bool:
    if len(password) < 8:
        return False
    has_digit = any(ch.isdigit() for ch in password)
    has_upper = any(ch.isupper() for ch in password)
    return has_digit and has_upper


# STEP 1: Failing Tests Written FIRST (RED)
def test_password_short_fails() -> None:
    assert is_password_strong("Pass1") is False


def test_password_no_digit_fails() -> None:
    assert is_password_strong("Password") is False


def test_password_no_upper_fails() -> None:
    assert is_password_strong("password123") is False


def test_valid_password_passes() -> None:
    assert is_password_strong("SecurePass123") is True


if __name__ == "__main__":
    test_password_short_fails()
    test_password_no_digit_fails()
    test_password_no_upper_fails()
    test_valid_password_passes()
    print("TDD suite for password strength validator passed!")
