"""
Topic: Conditionals Solutions
File: 05_solution.py
"""

def level_1_easy() -> None:
    num = 7
    parity = "even" if num % 2 == 0 else "odd"
    print(f"Number {num} is {parity}")


def level_2_medium(year: int) -> bool:
    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    print(f"Is year {year} a leap year? {is_leap}")
    return is_leap


def level_3_hard(income: float) -> float:
    if income <= 10000:
        rate = 0.0
    elif income <= 50000:
        rate = 0.10
    elif income <= 100000:
        rate = 0.20
    else:
        rate = 0.30
    print(f"Income: ${income:,.2f} -> Tax Rate: {rate:.0%}")
    return rate


def level_4_real_world(code: int) -> str:
    if 200 <= code <= 299:
        category = "SUCCESS"
    elif 400 <= code <= 499:
        category = "CLIENT_ERROR"
    elif 500 <= code <= 599:
        category = "SERVER_ERROR"
    else:
        category = "UNKNOWN_STATUS"
    print(f"HTTP {code} -> Category: {category}")
    return category


if __name__ == "__main__":
    print("--- Level 1 ---")
    level_1_easy()

    print("\n--- Level 2 ---")
    level_2_medium(2024)
    level_2_medium(1900)
    level_2_medium(2000)

    print("\n--- Level 3 ---")
    level_3_hard(45000.0)
    level_3_hard(120000.0)

    print("\n--- Level 4 ---")
    level_4_real_world(200)
    level_4_real_world(404)
    level_4_real_world(503)
