"""
AI NumPy Common Pitfalls.
"""

# MISTAKE: Fitting feature scaling parameters (mean/std) on the ENTIRE dataset before train/test splitting.
# WHY: Causes Data Leakage! Test set statistical information leaks into model training.
# FIX: Compute mean and std ONLY on training set (`X_train`), then transform `X_test` using `X_train` parameters.

if __name__ == "__main__":
    print("AI/ML data leakage prevention rules verified.")
