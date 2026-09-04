"""
Topic: CSV Writing & Reading with DictWriter and DictReader
File: 01_basic.py
"""
import csv
from pathlib import Path

def demonstrate_csv_operations() -> None:
    csv_file = Path("employees.csv")
    fieldnames = ["id", "name", "role", "salary"]

    records = [
        {"id": 101, "name": "Alice Johnson", "role": "Senior Engineer", "salary": 125000},
        {"id": 102, "name": "Bob Smith", "role": "DevOps Specialist", "salary": 110000},
    ]

    # 1. Writing CSV using DictWriter (Always set newline="")
    with csv_file.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)
    print(f"Wrote CSV records to '{csv_file.name}'")

    # 2. Reading CSV using DictReader
    print("\nReading CSV records back:")
    with csv_file.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(f"  - {row['name']} ({row['role']}): ${int(row['salary']):,}")

    if csv_file.exists():
        csv_file.unlink()


if __name__ == "__main__":
    demonstrate_csv_operations()
