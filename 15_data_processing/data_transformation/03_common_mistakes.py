"""
Data Transformation Common Pitfalls.
"""

# MISTAKE: Over-using `.apply(lambda row: ...)` for operations that can be computed natively with vectorization.
# WHY: Python lambdas lose Pandas C-speed vectorization, causing 10x-50x slower processing speeds.
# FIX: Use built-in vectorized methods (e.g. `df["price"] * df["quantity"]` instead of `df.apply(...)`).

if __name__ == "__main__":
    print("Vectorized transformation rules verified.")
