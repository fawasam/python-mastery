"""
Topic: Loops & Iteration Basics
File: 01_basic.py
"""

def demonstrate_for_and_while_loops() -> None:
    # 1. for loop with range(start, stop, step)
    print("--- 1. range(1, 10, 2) ---")
    for i in range(1, 10, 2):
        print(f"Step value: {i}")

    # 2. Iterating over a string sequence
    print("\n--- 2. Character Iteration ---")
    for char in "PYTHON":
        print(f"Char: {char}")

    # 3. while loop with a counter
    print("\n--- 3. while loop countdown ---")
    countdown = 3
    while countdown > 0:
        print(f"Countdown: {countdown}")
        countdown -= 1
    print("Blastoff!")


if __name__ == "__main__":
    demonstrate_for_and_while_loops()
