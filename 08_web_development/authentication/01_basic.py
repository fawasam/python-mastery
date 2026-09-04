"""
Secure Password Hashing and Salt Verification using PBKDF2.
"""

import hashlib
import hmac
import os


def hash_password(plain_password: str) -> tuple[bytes, str]:
    """Hashes password using PBKDF2-HMAC-SHA256 with 100,000 iterations and a random salt."""
    salt = os.urandom(16)
    key = hashlib.pbkdf2_hmac("sha256", plain_password.encode("utf-8"), salt, 100_000)
    return salt, key.hex()


def verify_password(plain_password: str, salt: bytes, expected_hash_hex: str) -> bool:
    """Verifies candidate plain password against stored salt and hash."""
    key = hashlib.pbkdf2_hmac("sha256", plain_password.encode("utf-8"), salt, 100_000)
    # Use hmac.compare_digest for constant-time string comparison (prevents timing attacks!)
    return hmac.compare_digest(key.hex(), expected_hash_hex)


if __name__ == "__main__":
    salt, password_hash = hash_password("SuperSecretPass123")
    print(f"Generated Salt (hex): {salt.hex()}")
    print(f"Hashed Key    (hex): {password_hash}")

    assert verify_password("SuperSecretPass123", salt, password_hash) is True
    assert verify_password("WrongPassword", salt, password_hash) is False
    print("Password hashing and verification passed successfully!")
