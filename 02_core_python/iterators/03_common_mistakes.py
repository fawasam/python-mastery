"""
Topic: Common Mistakes with Iterators
File: 03_common_mistakes.py
"""

def mistake_1_reusing_exhausted_iterator() -> None:
    data = [1, 2, 3]
    it = iter(data)

    # First loop consumes iterator
    list1 = list(it)
    # Second loop gets NOTHING
    list2 = list(it)

    print(f"List 1: {list1} | List 2 (Exhausted): {list2}")
    print("Remember: Iterators cannot be reset. Create a new iterator via iter() to re-iterate.")


if __name__ == "__main__":
    mistake_1_reusing_exhausted_iterator()
