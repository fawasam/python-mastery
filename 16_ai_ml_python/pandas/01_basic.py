"""
Pandas for ML Basics: Preparing Feature Matrix X and Target Vector y.
"""

import pandas as pd


def prepare_ml_dataset(df: pd.DataFrame, target_column: str) -> tuple[pd.DataFrame, pd.Series]:
    """
    Separate feature dataframe X from target variable series y.
    
    Returns (X, y).
    """
    X = df.drop(columns=[target_column])
    y = df[target_column]
    return X, y


if __name__ == "__main__":
    data = pd.DataFrame({
        "feature_age": [25, 30, 45],
        "feature_score": [80.5, 92.0, 75.0],
        "target_churn": [0, 1, 0]
    })
    
    X, y = prepare_ml_dataset(data, "target_churn")
    print("Feature Matrix X:\n", X)
    print("\nTarget Vector y:\n", y)
