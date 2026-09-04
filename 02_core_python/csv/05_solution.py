"""
Topic: CSV Solutions
File: 05_solution.py
"""
import csv
from pathlib import Path

def level_1_easy() -> None:
    csv_file = Path("products.csv")
    data = [("Item", "Price"), ("Laptop", 1200), ("Mouse", 25)]
    with csv_file.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(data)
    print(f"Wrote products to '{csv_file.name}'")


def level_2_medium() -> float:
    csv_file = Path("products.csv")
    if not csv_file.exists():
        level_1_easy()

    prices = []
    with csv_file.open("r", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)  # Skip header
        for row in reader:
            if len(row) >= 2:
                prices.append(float(row[1]))

    avg_price = sum(prices) / len(prices) if prices else 0.0
    print(f"Average price from CSV: ${avg_price:.2f}")
    
    if csv_file.exists():
        csv_file.unlink()
    return avg_price


def transform_sales_csv(input_path: Path, output_path: Path, tax_rate: float = 0.08) -> None:
    if not input_path.exists():
        return

    fieldnames = ["id", "item", "raw_amount", "clean_amount", "tax_amount", "total"]
    transformed_records = []

    with input_path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            raw_str = row.get("amount", "0").replace("$", "").replace(",", "").strip()
            clean_amt = float(raw_str)
            tax_amt = clean_amt * tax_rate
            total = clean_amt + tax_amt

            transformed_records.append({
                "id": row.get("id", ""),
                "item": row.get("item", ""),
                "raw_amount": row.get("amount", ""),
                "clean_amount": f"{clean_amt:.2f}",
                "tax_amount": f"{tax_amt:.2f}",
                "total": f"{total:.2f}",
            })

    with output_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(transformed_records)
    print(f"Transformed sales ETL written to '{output_path.name}'")


if __name__ == "__main__":
    print("--- Level 1 & 2 ---")
    level_2_medium()

    print("\n--- Level 4 (ETL Transformer) ---")
    src = Path("raw_sales.csv")
    dst = Path("clean_sales.csv")

    with src.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "item", "amount"])
        writer.writeheader()
        writer.writerows([
            {"id": "1", "item": "Keyboard", "amount": "$1,200.50"},
            {"id": "2", "item": "Mouse", "amount": "$45.00"},
        ])

    transform_sales_csv(src, dst)

    if src.exists():
        src.unlink()
    if dst.exists():
        dst.unlink()
