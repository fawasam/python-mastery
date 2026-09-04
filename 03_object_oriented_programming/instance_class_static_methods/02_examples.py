"""
Topic: Static Method Validator Helper Pattern
File: 02_examples.py
"""

class EmailValidator:
    @staticmethod
    def is_valid_email(email: str) -> bool:
        return "@" in email and "." in email.split("@")[-1]


if __name__ == "__main__":
    print(f"is 'user@domain.com' valid? {EmailValidator.is_valid_email('user@domain.com')}")
    print(f"is 'invalid_email' valid?   {EmailValidator.is_valid_email('invalid_email')}")
