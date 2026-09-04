"""
Solutions: Data Analysis Exercises.
"""

import pandas as pd


def compute_column_stats(df: pd.DataFrame, column: str) -> dict[str, float]:
    col = df[column]
    return {
        "mean": float(col.mean()),
        "median": float(col.median()),
        "std": float(col.std())
    }


if __name__ == "__main__":
    test_df = pd.DataFrame({"val": [10.0, 20.0, 30.0, 40.0, 50.0]})
    stats = compute_column_stats(test_df, "val")
    print("Column statistics:", stats)
