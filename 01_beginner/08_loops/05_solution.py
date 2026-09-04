"""
Topic: Loop Solutions
File: 05_solution.py
"""

def level_1_easy() -> int:
    total = 0
    for i in range(1, 51):
        total += i
    print(f"Sum 1 to 50: {total}")
    return total


def level_2_medium() -> None:
    num = 7
    print(f"Multiplication Table for {num}:")
    for i in range(1, 11):
        print(f"{num} x {i:>2} = {num * i:>2}")


def level_3_hard() -> list[int]:
    primes = []
    for num in range(2, 31):
        for divisor in range(2, int(num**0.5) + 1):
            if num % divisor == 0:
                break
        else:
            primes.append(num)
    print(f"Primes (2..30): {primes}")
    return primes


def level_4_real_world(max_attempts: int = 5) -> bool:
    for attempt in range(1, max_attempts + 1):
        print(f"Attempt {attempt}/{max_attempts}: Connecting to server...")
        if attempt == 4:
            print("✅ Connection established successfully!")
            return True
        print("⚡ Connection refused. Retrying...")
    else:
        print("❌ Error: Maximum retry attempts reached. Server unreachable.")
        return False


if __name__ == "__main__":
    print("--- Level 1 ---")
    level_1_easy()

    print("\n--- Level 2 ---")
    level_2_medium()

    print("\n--- Level 3 ---")
    level_3_hard()

    print("\n--- Level 4 ---")
    level_4_real_world()
