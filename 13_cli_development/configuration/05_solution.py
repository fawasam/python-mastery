"""
Solutions: Configuration Exercises.
"""

import os


def load_env_int(key: str, default: int) -> int:
    val = os.getenv(key)
    if val is None:
        return default
    try:
        return int(val)
    except ValueError:
        return default


if __name__ == "__main__":
    print("Parsed int env fallback:", load_env_int("NON_EXISTENT_PORT", 8080))
