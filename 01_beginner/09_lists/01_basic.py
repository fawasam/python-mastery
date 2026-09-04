"""
Topic: Lists Basics & Operations
File: 01_basic.py
"""

def demonstrate_list_operations() -> None:
    # 1. Initialization
    scores: list[int] = [88, 92, 79, 95]
    print(f"Initial list: {scores}")

    # 2. Appending and inserting
    scores.append(100)           # Adds to end
    scores.insert(1, 85)         # Inserts at index 1
    print(f"After append & insert: {scores}")

    # 3. Removing items
    last_item = scores.pop()     # Removes and returns last item (100)
    print(f"Popped item: {last_item} | List after pop: {scores}")

    scores.remove(79)            # Removes first occurrence of 79
    print(f"After removing 79: {scores}")

    # 4. Sorting
    scores.sort()                # In-place sort ascending
    print(f"Sorted in-place: {scores}")


if __name__ == "__main__":
    demonstrate_list_operations()
