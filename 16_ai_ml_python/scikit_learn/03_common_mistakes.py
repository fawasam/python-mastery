"""
Scikit-Learn Common Pitfalls.
"""

# MISTAKE: Calling `.fit_transform()` on the test dataset (`X_test`).
# WHY: Calling `.fit_transform()` re-calculates mean/std on test data instead of using training set scaling parameters.
# FIX: Always call `.fit_transform()` on `X_train`, but ONLY `.transform()` on `X_test`.

if __name__ == "__main__":
    print("Scikit-Learn transform rules verified.")
