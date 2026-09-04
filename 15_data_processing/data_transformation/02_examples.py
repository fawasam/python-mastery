"""
Advanced Data Transformation: Pivot Tables and Un-pivoting (Melt).
"""

import pandas as pd


def demonstrate_pivot_and_melt() -> None:
    # Transaction dataset
    df = pd.DataFrame({
        "year": [2025, 2025, 2026, 2026],
        "quarter": ["Q1", "Q2", "Q1", "Q2"],
        "revenue": [100.0, 120.0, 150.0, 180.0]
    })

    # Pivot table: reshape long format into wide format
    pivot_df = df.pivot(index="year", columns="quarter", values="revenue")
    print("=== Pivoted DataFrame (Wide Format) ===")
    print(pivot_df)

    # Melt: reshape wide format back to long format
    reset_pivot = pivot_df.reset_index()
    melted_df = pd.melt(reset_pivot, id_vars=["year"], value_vars=["Q1", "Q2"], var_name="quarter", value_name="revenue")
    print("\n=== Melted DataFrame (Long Format) ===")
    print(melted_df)


if __name__ == "__main__":
    demonstrate_pivot_and_melt()
