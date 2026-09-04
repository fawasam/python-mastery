"""
Pandas Basics: DataFrame Creation, Selection, and Filtering.
"""

import pandas as pd


def demonstrate_pandas_basics() -> None:
    # 1. Create DataFrame from dictionary
    data = {
        "name": ["Alice", "Bob", "Charlie", "David"],
        "department": ["Engineering", "Sales", "Engineering", "Marketing"],
        "salary": [95000, 70000, 105000, 65000],
        "years_experience": [4, 2, 7, 3]
    }
    df = pd.DataFrame(data)
    print("=== Initial DataFrame ===")
    print(df)

    # 2. Filtering with boolean masks
    eng_df = df[df["department"] == "Engineering"]
    print("\n=== Engineering Department ===")
    print(eng_df)

    # 3. Aggregation via groupby
    avg_salary = df.groupby("department")["salary"].mean().reset_index()
    print("\n=== Average Salary by Department ===")
    print(avg_salary)


if __name__ == "__main__":
    demonstrate_pandas_basics()
