"""
Advanced Pandas: Merging, Pivoting, and Handling Missing Data.
"""

import pandas as pd


def demonstrate_pandas_advanced() -> None:
    # 1. Handling Missing (NaN) Data
    raw_data = {
        "user_id": [101, 102, 103, 104],
        "age": [25, None, 30, 45],
        "score": [88.5, 92.0, None, 78.0]
    }
    df = pd.DataFrame(raw_data)
    print("=== Raw DataFrame with NaNs ===")
    print(df)

    # Fill missing ages with median age
    df["age"] = df["age"].fillna(df["age"].median())
    # Drop rows with missing scores
    cleaned_df = df.dropna(subset=["score"])
    
    print("\n=== Cleaned DataFrame ===")
    print(cleaned_df)


if __name__ == "__main__":
    demonstrate_pandas_advanced()
