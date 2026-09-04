"""
Solutions: Pandas Exercises.
"""

import pandas as pd


def filter_top_performers(df: pd.DataFrame, score_column: str, threshold: float) -> pd.DataFrame:
    return df[df[score_column] > threshold]


if __name__ == "__main__":
    test_df = pd.DataFrame({"name": ["Alice", "Bob"], "score": [95.0, 75.0]})
    top = filter_top_performers(test_df, "score", 80.0)
    print("Top performers:\n", top)
