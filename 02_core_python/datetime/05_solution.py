"""
Topic: Datetime Solutions
File: 05_solution.py
"""
from datetime import date, datetime, timedelta, timezone

def level_1_easy() -> int:
    d1 = date(2026, 1, 1)
    d2 = date(2026, 12, 31)
    delta = (d2 - d1).days
    print(f"Days between {d1} and {d2}: {delta} days")
    return delta


def level_2_medium() -> datetime:
    date_str = "04/Sep/2026 14:30"
    parsed = datetime.strptime(date_str, "%d/%b/%Y %H:%M")
    print(f"Parsed datetime: {parsed}")
    return parsed


def level_3_hard(created_at: datetime, ttl_seconds: int = 3600) -> bool:
    now = datetime.now(timezone.utc) if created_at.tzinfo else datetime.now()
    is_expired = (now - created_at).total_seconds() > ttl_seconds
    print(f"Token created {created_at.isoformat()} expired? {is_expired}")
    return is_expired


def level_4_real_world(start_date: date, num_days: int) -> date:
    current = start_date
    added = 0
    while added < num_days:
        current += timedelta(days=1)
        # Monday=0, ..., Sunday=6. Weekends are 5 and 6
        if current.weekday() < 5:
            added += 1
    print(f"Added {num_days} business days to {start_date} -> {current}")
    return current


if __name__ == "__main__":
    print("--- Level 1 ---")
    level_1_easy()

    print("\n--- Level 2 ---")
    level_2_medium()

    print("\n--- Level 3 ---")
    level_3_hard(datetime.now(timezone.utc) - timedelta(seconds=4000))

    print("\n--- Level 4 ---")
    level_4_real_world(date(2026, 9, 4), 5)  # 5 business days
