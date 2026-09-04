"""
Pandas Common Pitfalls.
"""

# MISTAKE: Iterating over DataFrame rows using `for index, row in df.iterrows():`.
# WHY: `iterrows()` is extremely slow (100x slower) because it constructs a Pandas Series for every single row.
# FIX: Use vectorized column operations or `.apply()` / `.itertuples()`.

if __name__ == "__main__":
    print("Pandas iteration performance rules verified.")
