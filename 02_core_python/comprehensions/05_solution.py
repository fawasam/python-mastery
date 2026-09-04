"""
Topic: Comprehension Solutions
File: 05_solution.py
"""

def level_1_easy() -> list[int]:
    cubes = [x**3 for x in range(1, 11)]
    print(f"Cubes 1..10: {cubes}")
    return cubes


def level_2_medium(words: list[str]) -> dict[str, int]:
    result = {w: len(w) for w in words if w.lower().startswith("a")}
    print(f"A-words length dict: {result}")
    return result


def level_3_hard(matrix: list[list[int]]) -> list[list[int]]:
    transposed = [[row[col] for row in matrix] for col in range(len(matrix[0]))]
    print(f"Original: {matrix} -> Transposed: {transposed}")
    return transposed


def level_4_real_world(users: list[dict[str, str | bool]]) -> list[str]:
    active_emails = [str(u["email"]).lower() for u in users if u.get("active") and "email" in u]
    print(f"Active user emails: {active_emails}")
    return active_emails


if __name__ == "__main__":
    print("--- Level 1 ---")
    level_1_easy()

    print("\n--- Level 2 ---")
    level_2_medium(["apple", "banana", "apricot", "cherry", "avocado"])

    print("\n--- Level 3 ---")
    level_3_hard([[1, 2], [3, 4], [5, 6]])

    print("\n--- Level 4 ---")
    users = [
        {"email": "ALICE@DEV.IO", "active": True},
        {"email": "bob@dev.io", "active": False},
        {"email": "CHARLIE@DEV.IO", "active": True},
    ]
    level_4_real_world(users)
