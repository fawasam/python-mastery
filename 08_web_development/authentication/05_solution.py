"""
Solutions for Authentication Exercises.
"""

import hmac


def verify_bearer_token(received_token: str, expected_token: str) -> bool:
    if not received_token or not expected_token:
        return False
    return hmac.compare_digest(received_token.encode("utf-8"), expected_token.encode("utf-8"))


if __name__ == "__main__":
    assert verify_bearer_token("bearer_secret_123", "bearer_secret_123") is True
    assert verify_bearer_token("wrong_token", "bearer_secret_123") is False
    print("Bearer token verification exercise passed successfully!")
