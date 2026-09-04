"""
Solutions: Scikit-Learn Exercises.
"""

import numpy as np
from sklearn.metrics import accuracy_score


def compute_accuracy(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    return float(accuracy_score(y_true, y_pred))


if __name__ == "__main__":
    y_t = np.array([1, 0, 1, 1, 0])
    y_p = np.array([1, 0, 1, 0, 0])
    acc = compute_accuracy(y_t, y_p)
    print("Accuracy Score:", acc)
