"""
Data Processing Mini Project: E-Commerce Sales Pipeline.
"""

import pandas as pd


def generate_raw_sales_dataset() -> pd.DataFrame:
    """Generate synthetic messy sales records."""
    return pd.DataFrame({
        "order_id": ["ORD-1", "ORD-2", "ORD-3", "ORD-4", "ORD-4"],  # Contains duplicate ORD-4
        "category": [" Electronics ", "Clothing", "ELECTRONICS", " home ", " home "],
        "price": [299.99, 49.50, 150.00, None, 89.99],
        "quantity": [1, 2, 1, 3, 3],
        "order_date": ["2026-01-10", "2026-01-11", "2026-01-12", "2026-01-15", "2026-01-15"]
    })


def run_etl_pipeline(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Execute cleaning, transformation, and aggregation steps."""
    cleaned = df.copy()

    # 1. Clean categorical text
    cleaned["category"] = cleaned["category"].str.strip().str.capitalize()

    # 2. Impute missing price with median category price
    median_price = cleaned["price"].median()
    cleaned["price"] = cleaned["price"].fillna(median_price)

    # 3. Deduplicate exact duplicate order records
    cleaned = cleaned.drop_duplicates(subset=["order_id"])

    # 4. Feature engineering: compute total sale value
    cleaned["total_sale"] = cleaned["price"] * cleaned["quantity"]
    cleaned["order_date"] = pd.to_datetime(cleaned["order_date"])

    # 5. Category analytics summary
    category_summary = cleaned.groupby("category").agg(
        total_revenue=("total_sale", "sum"),
        average_order_value=("total_sale", "mean"),
        total_orders=("order_id", "count")
    ).reset_index()

    return cleaned, category_summary


def main() -> None:
    print("=== Raw Input Sales Dataset ===")
    raw_df = generate_raw_sales_dataset()
    print(raw_df)

    print("\n=== Running E-Commerce ETL Data Pipeline ===")
    cleaned_df, summary_df = run_etl_pipeline(raw_df)

    print("\n=== Cleaned & Transformed Dataset ===")
    print(cleaned_df[["order_id", "category", "price", "quantity", "total_sale"]])

    print("\n=== Category Analytics Summary ===")
    print(summary_df)


if __name__ == "__main__":
    main()
