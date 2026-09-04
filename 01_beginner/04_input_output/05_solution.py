"""
Topic: Input & Output Solutions
File: 05_solution.py
"""

def level_1_easy() -> None:
    number = 78.12945
    print(f"Formatted: {number:.2f}")


def level_2_medium() -> None:
    population = 1250000
    print(f"Population: {population:,}")


def level_3_hard(name: str, qty: int, unit_price: float) -> str:
    total = qty * unit_price
    formatted_line = f"{name:<15} | {qty:^5d} | ${total:>10.2f}"
    print(formatted_line)
    return formatted_line


def level_4_real_world(cpu: float, mem_used: float, mem_total: float, reqs: int) -> str:
    dashboard = f"""================ SYSTEM METRICS ================
CPU Usage:        {cpu:.1f}%
Memory Usage:     {mem_used:.2f} GB / {mem_total:.2f} GB
Total Requests:   {reqs:,}
================================================="""
    print(dashboard)
    return dashboard


if __name__ == "__main__":
    print("--- Level 1 ---")
    level_1_easy()

    print("\n--- Level 2 ---")
    level_2_medium()

    print("\n--- Level 3 ---")
    level_3_hard("Mechanical Keyboard", 2, 89.50)

    print("\n--- Level 4 ---")
    level_4_real_world(74.2, 12.45, 16.0, 1450200)
