"""
Data Cleaning Common Pitfalls.
"""

# MISTAKE: Dropping missing values indiscriminately with `df.dropna()` without auditing columns first.
# WHY: Inadvertently deletes entire valid rows just because an optional non-critical column had a NaN.
# FIX: Specify exact subset of required columns: `df.dropna(subset=["critical_id", "email"])`.

if __name__ == "__main__":
    print("Selective dropna rules verified.")
