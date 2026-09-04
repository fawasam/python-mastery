"""
Topic: List Solutions
File: 05_solution.py
"""

def level_1_easy() -> list[int]:
    nums = [10, 20, 30, 40, 50]
    nums.remove(30)
    nums.insert(2, 35)
    print(f"Modified list: {nums}")
    return nums


def level_2_medium(items: list[int]) -> list[int]:
    seen = set()
    unique_items = []
    for item in items:
        if item not in seen:
            seen.add(item)
            unique_items.append(item)
    print(f"Original: {items} -> Order-preserved unique: {unique_items}")
    return unique_items


def level_3_hard(students: list[tuple[str, int]]) -> list[tuple[str, int]]:
    sorted_students = sorted(students, key=lambda student: student[1], reverse=True)
    print("Sorted by grade descending:", sorted_students)
    return sorted_students


def level_4_real_world(data: list[float], window_size: int) -> list[float]:
    if window_size <= 0 or window_size > len(data):
        raise ValueError("Invalid window size")
    averages = []
    for i in range(len(data) - window_size + 1):
        window = data[i : i + window_size]
        avg = sum(window) / window_size
        averages.append(round(avg, 2))
    print(f"Moving Average (window={window_size}): {averages}")
    return averages


if __name__ == "__main__":
    print("--- Level 1 ---")
    level_1_easy()

    print("\n--- Level 2 ---")
    level_2_medium([1, 2, 2, 3, 4, 4, 5])

    print("\n--- Level 3 ---")
    level_3_hard([("Alice", 88), ("Bob", 95), ("Charlie", 78)])

    print("\n--- Level 4 ---")
    level_4_real_world([10.0, 20.0, 30.0, 40.0, 50.0], 3)
