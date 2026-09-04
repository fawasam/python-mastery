"""
Solutions: NumPy for ML Exercises.
"""

import numpy as np


def mean_squared_error(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    return float(np.mean((y_true - y_pred) ** 2))


if __name__ == "__main__":
    y_t = np.array([3.0, -0.5, 2.0, 7.0])
    y_p = np.array([2.5, 0.0, 2.0, 8.0])
    mse = mean_squared_error(y_t, y_p)
    print("Calculated MSE Loss:", mse)
