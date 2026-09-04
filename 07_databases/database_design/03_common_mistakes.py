"""
Common Mistakes in Database Design.
"""


# MISTAKE 1: Denormalization bug - Storing comma-separated lists in single string column
def mistake_csv_in_column() -> None:
    # DANGER: Storing tags as "python,django,web" in a single column violates 1NF (First Normal Form)!
    # Makes filtering, querying, and indexing individual tags virtually impossible or slow!
    pass


if __name__ == "__main__":
    print("Always adhere to 1NF: Every column must contain atomic (indivisible) scalar values!")
