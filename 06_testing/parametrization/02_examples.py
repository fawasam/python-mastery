"""
Parametrized Email Validation Example.
"""

import re

EMAIL_REGEX = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$")


def validate_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    return bool(EMAIL_REGEX.match(email.strip()))


def test_email_validation_cases() -> None:
    valid_emails = [
        "alice@example.com",
        "bob.smith@company.co.uk",
        "user123@domain.org",
    ]
    invalid_emails = [
        "plainaddress",
        "@missinguser.com",
        "user@.com",
        "user@domain",
    ]

    for email in valid_emails:
        assert validate_email(email) is True, f"Expected {email} to be VALID"

    for email in invalid_emails:
        assert validate_email(email) is False, f"Expected {email} to be INVALID"

    print("All email validation test cases passed successfully.")


if __name__ == "__main__":
    test_email_validation_cases()
