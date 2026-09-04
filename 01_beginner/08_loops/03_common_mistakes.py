"""
Topic: Common Mistakes with Loops
File: 03_common_mistakes.py
"""

def mistake_1_infinite_while_loop() -> None:
    # ❌ WRONG: Forgetting to update loop control condition inside while loop
    # count = 0
    # while count < 5:
    #     print(count)  # Never increments -> Infinite loop!
    
    # ✅ CORRECT: Update control condition on each pass
    count = 0
    while count < 3:
        print(f"Safe count: {count}")
        count += 1


def mistake_2_modifying_list_while_iterating() -> None:
    numbers = [1, 2, 3, 4, 5, 6]

    # ❌ WRONG: Modifying list during iteration causes skipped elements!
    # for item in numbers:
    #     if item % 2 == 0:
    #         numbers.remove(item)

    # ✅ CORRECT: Iterate over a slice copy `numbers[:]` or use list comprehension
    clean_numbers = [num for num in numbers if num % 2 != 0]
    print(f"Filtered numbers: {clean_numbers}")


if __name__ == "__main__":
    mistake_1_infinite_while_loop()
    mistake_2_modifying_list_while_iterating()
