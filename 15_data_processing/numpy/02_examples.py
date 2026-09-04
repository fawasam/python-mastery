"""
Advanced NumPy: Matrix Multiplication and Broadcasting.
"""

import numpy as np


def demonstrate_matrix_operations() -> None:
    # 2x3 Matrix
    matrix_a = np.array([[1, 2, 3], [4, 5, 6]])
    # 3x2 Matrix
    matrix_b = np.array([[7, 8], [9, 10], [11, 12]])

    # Matrix multiplication using @ operator
    product = matrix_a @ matrix_b
    print("Matrix Product (2x3 @ 3x2 -> 2x2):\n", product)

    # Broadcasting example: adding 1D array to 2D matrix
    row_vector = np.array([10, 20])
    broadcasted_sum = product + row_vector
    print("\nBroadcasted Sum:\n", broadcasted_sum)


if __name__ == "__main__":
    demonstrate_matrix_operations()
