"""
Crypto Utilities for Password Hashing and Masking.
"""

import base64
import hashlib
import hmac


def hash_password(password: str, salt: bytes) -> str:
    """Hash password using SHA-256 with salt."""
    key = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 100000)
    return base64.b64encode(key).decode("utf-8")


def verify_password(password: str, salt: bytes, hashed: str) -> bool:
    """Verify password matches hash using constant-time comparison."""
    computed = hash_password(password, salt)
    return hmac.compare_digest(computed, hashed)
