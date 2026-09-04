"""
Solutions for Optimization Exercises.
"""


def find_common_elements(list_a: list[int], list_b: list[int]) -> list[int]:
    set_b = set(list_b)
    return [x for x in list_a if x in set_b]


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5]
    b = [3, 4, 5, 6, 7]
    common = find_common_elements(a, b)
    assert common == [3, 4, 5]
    print(f"O(N) Set intersection exercise passed! Common elements: {common}")
