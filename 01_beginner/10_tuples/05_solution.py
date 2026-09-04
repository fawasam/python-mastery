"""
Topic: Tuple Solutions
File: 05_solution.py
"""

def level_1_easy() -> None:
    dob = (1995, 10, 24)
    year, month, day = dob
    print(f"DOB Unpacked -> Year: {year}, Month: {month}, Day: {day}")


def level_2_medium() -> None:
    numbers = [1, 2, 3, 4, 5, 6]
    first, *middle, last = numbers
    print(f"First: {first} | Middle: {middle} | Last: {last}")


def level_3_hard(numbers: list[float]) -> tuple[float, float, float]:
    if not numbers:
        raise ValueError("List cannot be empty")
    min_val = min(numbers)
    max_val = max(numbers)
    avg_val = sum(numbers) / len(numbers)
    result = (min_val, max_val, round(avg_val, 2))
    print(f"Stats (min, max, avg): {result}")
    return result


def level_4_real_world() -> tuple[tuple[str, int, str], ...]:
    db_clusters = (
        ("db-primary.internal", 5432, "READ_WRITE"),
        ("db-replica-1.internal", 5432, "READ_ONLY"),
        ("db-replica-2.internal", 5432, "READ_ONLY"),
    )
    for host, port, mode in db_clusters:
        print(f"Node [{mode}]: {host}:{port}")
    return db_clusters


if __name__ == "__main__":
    print("--- Level 1 ---")
    level_1_easy()

    print("\n--- Level 2 ---")
    level_2_medium()

    print("\n--- Level 3 ---")
    level_3_hard([10.5, 20.0, 15.5, 40.0])

    print("\n--- Level 4 ---")
    level_4_real_world()
