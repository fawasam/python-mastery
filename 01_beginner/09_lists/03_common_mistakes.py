"""
Topic: Common Mistakes with Lists
File: 03_common_mistakes.py
"""

def mistake_1_expecting_in_place_sort_to_return_list() -> None:
    numbers = [5, 2, 8, 1]

    # ❌ WRONG: sorted_nums = numbers.sort()
    # numbers.sort() returns None! sorted_nums becomes None!
    
    # ✅ CORRECT: Use numbers.sort() in-place OR use sorted(numbers) to assign
    sorted_new_list = sorted(numbers)
    print(f"Original: {numbers} | New sorted list: {sorted_new_list}")


def mistake_2_index_out_of_range() -> None:
    items = ["a", "b", "c"]
    
    # ❌ WRONG: print(items[3]) -> IndexError: list index out of range
    # In a 3-element list, valid positive indices are 0, 1, 2.
    
    # ✅ CORRECT: Check len() or use exception handling
    if len(items) > 3:
        print(items[3])
    else:
        print("Index 3 is out of range for items.")


if __name__ == "__main__":
    mistake_1_expecting_in_place_sort_to_return_list()
    mistake_2_index_out_of_range()
