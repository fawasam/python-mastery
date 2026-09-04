"""
Data Transformation Basics: One-Hot Encoding and Value Binning.
"""

import pandas as pd


def demonstrate_transformations() -> None:
    df = pd.DataFrame({
        "customer_id": [1, 2, 3, 4],
        "tier": ["Bronze", "Gold", "Silver", "Gold"],
        "age": [19, 35, 62, 28]
    })
    print("=== Raw Customer DataFrame ===")
    print(df)

    # 1. One-Hot Encoding categorical 'tier'
    encoded_df = pd.get_dummies(df, columns=["tier"], prefix="tier", dtype=int)
    print("\n=== One-Hot Encoded Tiers ===")
    print(encoded_df)

    # 2. Binning age into generational brackets
    bins = [0, 25, 50, 100]
    labels = ["Young", "Adult", "Senior"]
    df["age_group"] = pd.cut(df["age"], bins=bins, labels=labels)
    print("\n=== Age Binned DataFrame ===")
    print(df[["customer_id", "age", "age_group"]])


if __name__ == "__main__":
    demonstrate_transformations()
