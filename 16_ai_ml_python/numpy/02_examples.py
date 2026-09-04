"""
Advanced AI NumPy: Feature Matrix Standard Scaling (Z-Score Standardization).
"""

import numpy as np


def standardize_features(X: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Standardize feature matrix X such that each column has mean=0 and std=1.
    
    Returns (scaled_X, mean_vector, std_vector).
    """
    mean = np.mean(X, axis=0)
    std = np.std(X, axis=0)
    
    # Avoid division by zero for constant features
    std[std == 0] = 1.0
    
    scaled_X = (X - mean) / std
    return scaled_X, mean, std


if __name__ == "__main__":
    # Synthetic dataset: 4 samples, 2 features (e.g. Age, Income)
    X_raw = np.array([
        [25.0, 50000.0],
        [45.0, 90000.0],
        [35.0, 75000.0],
        [50.0, 110000.0]
    ])
    
    X_scaled, mu, sigma = standardize_features(X_raw)
    print("Raw Feature Matrix X:\n", X_raw)
    print("\nStandardized Feature Matrix (Z-Score):\n", np.round(X_scaled, 3))
    print(f"\nScaled Feature Means: {np.round(np.mean(X_scaled, axis=0), 3)}")
    print(f"Scaled Feature Stds:  {np.round(np.std(X_scaled, axis=0), 3)}")
