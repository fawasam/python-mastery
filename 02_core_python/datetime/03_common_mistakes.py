"""
Topic: Common Mistakes with Datetime (Naive vs Aware)
File: 03_common_mistakes.py
"""
from datetime import datetime, timezone

def mistake_1_comparing_naive_and_aware_datetimes() -> None:
    naive_dt = datetime.now()  # No timezone info (Naive)
    aware_dt = datetime.now(timezone.utc)  # UTC info attached (Aware)

    # ❌ WRONG: naive_dt > aware_dt
    # Raises TypeError: can't compare offset-naive and offset-aware datetimes

    # ✅ CORRECT: Always work with explicit UTC timezone-aware datetimes in production!
    print("Always use datetime.now(timezone.utc) to prevent timezone comparison crashes.")


if __name__ == "__main__":
    mistake_1_comparing_naive_and_aware_datetimes()
