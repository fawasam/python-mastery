"""
Topic: Module Solutions
File: 05_solution.py
"""
import math
import os
import random
import sys
from collections import Counter

def level_1_easy() -> float:
    radius = 7.5
    area = math.pi * (radius ** 2)
    print(f"Area of circle (r={radius}): {area:.2f}")
    return round(area, 2)


def level_2_medium() -> int:
    seven_count = 0
    for _ in range(100):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        if die1 + die2 == 7:
            seven_count += 1
    print(f"Dice total of 7 occurred {seven_count} times out of 100 rolls.")
    return seven_count


def level_3_hard() -> list[tuple[str, int]]:
    text = "abracadabra"
    counter = Counter(text)
    top_3 = counter.most_common(3)
    print(f"Top 3 letters in '{text}': {top_3}")
    return top_3


def level_4_real_world() -> dict[str, str | int]:
    info = {
        "python_version": sys.version.split()[0],
        "platform": sys.platform,
        "cpu_count": os.cpu_count() or 1,
    }
    print(f"System Diagnostic Summary: {info}")
    return info


if __name__ == "__main__":
    print("--- Level 1 ---")
    level_1_easy()

    print("\n--- Level 2 ---")
    level_2_medium()

    print("\n--- Level 3 ---")
    level_3_hard()

    print("\n--- Level 4 ---")
    level_4_real_world()
