"""
Memory-Efficient Data Structures: array.array vs list.
"""

from array import array
import sys


def compare_array_vs_list() -> None:
    count = 100_000

    # Python list holds pointers to integer PyObjects
    py_list = list(range(count))

    # C-style compact typed array storing raw 4-byte integers in continuous C memory buffer
    c_array = array("i", range(count))

    list_size_kb = sys.getsizeof(py_list) / 1024.0
    array_size_kb = sys.getsizeof(c_array) / 1024.0

    print(f"Standard Python List Memory: {list_size_kb:.2f} KB")
    print(f"Typed array.array Memory  : {array_size_kb:.2f} KB")
    print(f"RAM Savings: {(1.0 - array_size_kb / list_size_kb) * 100:.1f}%")


if __name__ == "__main__":
    compare_array_vs_list()
