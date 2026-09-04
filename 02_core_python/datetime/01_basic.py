"""
Topic: Datetime Basics & Timezone Awareness
File: 01_basic.py
"""
from datetime import datetime, timedelta, timezone

def demonstrate_datetime() -> None:
    # 1. UTC Now (Timezone Aware)
    now_utc = datetime.now(timezone.utc)
    print(f"Current UTC: {now_utc.isoformat()}")

    # 2. strftime formatting
    formatted = now_utc.strftime("%A, %B %d, %Y - %I:%M %p")
    print(f"Formatted:   {formatted}")

    # 3. Timedelta arithmetic
    thirty_days_later = now_utc + timedelta(days=30)
    print(f"In 30 days:  {thirty_days_later.strftime('%Y-%m-%d')}")


if __name__ == "__main__":
    demonstrate_datetime()
