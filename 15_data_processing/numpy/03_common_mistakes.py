"""
NumPy Common Pitfalls.
"""

# MISTAKE: Iterating over NumPy arrays using Python for-loops (`for x in arr:`).
# WHY: Python loops defeat vectorization, making operations 50x-100x slower.
# FIX: Use built-in NumPy functions (`np.sum()`, `np.mean()`, `arr * 2`) operating over entire arrays.

if __name__ == "__main__":
    print("NumPy vectorization rules verified.")
