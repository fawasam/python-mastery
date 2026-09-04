"""
NumPy Basics: Array Creation, Vectorization, and Masking.
"""

import numpy as np


def demonstrate_numpy_vectorization() -> None:
    # 1. Array creation
    arr = np.array([1, 2, 3, 4, 5], dtype=np.int64)
    print("NumPy Array:", arr, "Shape:", arr.shape, "Dtype:", arr.dtype)

    # 2. Vectorized arithmetic (C-speed element-wise math)
    squared = arr ** 2
    print("Vectorized Squared Array:", squared)

    # 3. Boolean indexing / masking
    mask = arr > 2
    filtered = arr[mask]
    print("Filtered elements > 2:", filtered)


if __name__ == "__main__":
    demonstrate_numpy_vectorization()
