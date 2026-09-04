"""
Solutions: Pandas Feature Split Exercises.
"""

import pandas as pd


def split_features_target(df: pd.DataFrame, target_name: str) -> tuple[pd.DataFrame, pd.Series]:
    X = df.drop(columns=[target_name])
    y = df[target_name]
    return X, y


if __name__ == "__main__":
    data = pd.DataFrame({"feat1": [1, 2], "feat2": [3, 4], "label": [0, 1]})
    X, y = split_features_target(data, "label")
    print("X columns:", list(X.columns), "y name:", y.name)
