"""
Solutions: NumPy Exercises.
"""

import numpy as np


def normalize_array(arr: np.ndarray) -> np.ndarray:
    arr_min = np.min(arr)
    arr_max = np.max(arr)
    if arr_max == arr_min:
        return np.zeros_like(arr, dtype=np.float64)
    return (arr - arr_min) / (arr_max - arr_min)


if __name__ == "__main__":
    data = np.array([10.0, 20.0, 30.0, 40.0, 50.0])
    norm = normalize_array(data)
    print("Normalized array:", norm)
