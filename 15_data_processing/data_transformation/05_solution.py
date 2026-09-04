"""
Solutions: Data Transformation Exercises.
"""

import pandas as pd


def add_total_revenue_column(df: pd.DataFrame) -> pd.DataFrame:
    res = df.copy()
    res["total_revenue"] = res["price"] * res["quantity"]
    return res


if __name__ == "__main__":
    test_df = pd.DataFrame({"price": [10.0, 20.0], "quantity": [2, 5]})
    res_df = add_total_revenue_column(test_df)
    print("Transformed df:\n", res_df)
