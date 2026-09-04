"""
Solutions: C-API Concepts Exercises.
"""

import ctypes


def create_c_int_array(values: list[int]) -> ctypes.Array:
    array_type = ctypes.c_int * len(values)
    return array_type(*values)


if __name__ == "__main__":
    c_arr = create_c_int_array([1, 2, 3])
    print("C array length:", len(c_arr), "First element:", c_arr[0])
