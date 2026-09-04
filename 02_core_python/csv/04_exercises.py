"""
Topic: CSV Exercises
File: 04_exercises.py
"""

def level_1_easy() -> None:
    """
    Level 1 — Easy:
    Write a list of tuples `[("Item", "Price"), ("Laptop", 1200), ("Mouse", 25)]` to `products.csv` using `csv.writer`.
    """
    # TODO: Write CSV tuples
    raise NotImplementedError("Level 1 exercise not completed yet.")


def level_2_medium() -> None:
    """
    Level 2 — Medium:
    Read `products.csv` using `csv.reader` and calculate the average item price.
    """
    # TODO: Calculate average price from CSV
    raise NotImplementedError("Level 2 exercise not completed yet.")


def level_3_hard() -> None:
    """
    Level 3 — Hard:
    Filter a CSV file: read `input.csv` containing student records, filter records where `grade >= 80`, and write filtered records to `honors.csv` using `DictReader` and `DictWriter`.
    """
    # TODO: CSV filter pipeline
    raise NotImplementedError("Level 3 exercise not completed yet.")


def level_4_real_world() -> None:
    """
    Level 4 — Real World:
    Build an ETL CSV transformer function `transform_sales_csv(input_path: Path, output_path: Path)` that normalizes currency strings (e.g. `"$1,200.50"` -> `1200.50`) and adds a `tax_amount` column.
    """
    # TODO: ETL CSV transformer
    raise NotImplementedError("Level 4 exercise not completed yet.")


if __name__ == "__main__":
    print("--- Running Exercises ---")
    for lvl, fn in enumerate([level_1_easy, level_2_medium, level_3_hard, level_4_real_world], 1):
        try:
            fn()
        except NotImplementedError as e:
            print(f"Level {lvl}: {e}")
