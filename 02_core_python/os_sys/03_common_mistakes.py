"""
Topic: Common Mistakes with OS and Sys
File: 03_common_mistakes.py
"""
import os

def mistake_1_direct_environ_lookup() -> None:
    # ❌ WRONG: key = os.environ["OPTIONAL_SECRET"]
    # Raises KeyError if secret is not set in environment!

    # ✅ CORRECT: Use os.getenv(key, default) for optional variables
    secret = os.getenv("OPTIONAL_SECRET", "default_secret")
    print(f"Safe secret: {secret}")


if __name__ == "__main__":
    mistake_1_direct_environ_lookup()
