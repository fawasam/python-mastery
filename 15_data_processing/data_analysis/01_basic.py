"""
Exploratory Data Analysis Basics: Describing and Summarizing Data.
"""

import pandas as pd


def perform_summary_analysis() -> None:
    data = {
        "age": [22, 25, 47, 52, 46, 56, 55, 60],
        "income": [25000, 32000, 78000, 95000, 89000, 110000, 105000, 125000],
        "credit_score": [650, 710, 750, 810, 790, 820, 800, 850]
    }
    df = pd.DataFrame(data)

    print("=== Statistical Summary (describe) ===")
    print(df.describe())

    print("\n=== Correlation Matrix ===")
    print(df.corr())


if __name__ == "__main__":
    perform_summary_analysis()
