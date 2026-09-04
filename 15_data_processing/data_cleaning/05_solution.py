"""
Solutions: Data Cleaning Exercises.
"""

import pandas as pd


def fill_missing_numerical_with_mean(df: pd.DataFrame, column: str) -> pd.DataFrame:
    res = df.copy()
    col_mean = res[column].mean()
    res[column] = res[column].fillna(col_mean)
    return res


if __name__ == "__main__":
    test_df = pd.DataFrame({"val": [10.0, None, 30.0]})
    filled = fill_missing_numerical_with_mean(test_df, "val")
    print("Filled values:\n", filled)
