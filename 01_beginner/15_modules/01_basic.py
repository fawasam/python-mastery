"""
Topic: Modules & Standard Library Utilities
File: 01_basic.py
"""
import math
import random
from datetime import datetime, timezone

def demonstrate_standard_library() -> None:
    # 1. Math Module
    value = 16.0
    square_root = math.sqrt(value)
    print(f"math.sqrt({value}) = {square_root}")

    # 2. Random Module
    random_token = random.randint(100000, 999999)
    print(f"Generated 6-digit MFA Token: {random_token}")

    # 3. Datetime Module
    current_utc = datetime.now(timezone.utc)
    print(f"Current UTC Timestamp: {current_utc.isoformat()}")


if __name__ == "__main__":
    demonstrate_standard_library()
