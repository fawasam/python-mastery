"""
Advanced Pandas for ML: Encoding Categorical Features.
"""

import pandas as pd


def encode_categorical_features(df: pd.DataFrame, cat_cols: list[str]) -> pd.DataFrame:
    """One-hot encode categorical features into binary indicator columns."""
    return pd.get_dummies(df, columns=cat_cols, drop_first=True, dtype=int)


if __name__ == "__main__":
    df = pd.DataFrame({
        "income": [50000, 80000, 65000],
        "device": ["iOS", "Android", "iOS"]
    })
    encoded = encode_categorical_features(df, ["device"])
    print("Encoded ML Feature Set:\n", encoded)
