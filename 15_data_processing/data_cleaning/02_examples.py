"""
Advanced Data Cleaning: Outlier Detection using Interquartile Range (IQR).
"""

import pandas as pd


def remove_numerical_outliers_iqr(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """Filter out rows where column value lies beyond 1.5 * IQR bounds."""
    q1 = df[column].quantile(0.25)
    q3 = df[column].quantile(0.75)
    iqr = q3 - q1

    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]


if __name__ == "__main__":
    sales = pd.DataFrame({"transaction_id": range(1, 7), "amount": [10.0, 12.0, 15.0, 11.0, 14.0, 5000.0]})
    print("=== Raw Sales Data (contains outlier 5000) ===")
    print(sales)

    clean_sales = remove_numerical_outliers_iqr(sales, "amount")
    print("\n=== Clean Sales Data (outlier removed) ===")
    print(clean_sales)
