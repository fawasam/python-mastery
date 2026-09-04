"""
Data Cleaning Basics: Standardizing messy text and converting dates.
"""

import pandas as pd


def clean_raw_user_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """Clean dirty user dataframe by stripping whitespace, standardizing emails, and casting dates."""
    cleaned = df.copy()

    # Strip whitespace & lowercase emails
    cleaned["email"] = cleaned["email"].str.strip().str.lower()

    # Standardize names
    cleaned["name"] = cleaned["name"].str.strip().str.title()

    # Convert ISO strings to datetime
    cleaned["created_at"] = pd.to_datetime(cleaned["created_at"])

    # Remove exact duplicate rows
    cleaned = cleaned.drop_duplicates()

    return cleaned


if __name__ == "__main__":
    messy_data = {
        "name": [" alice smith ", "BOB JONES", "BOB JONES"],
        "email": ["ALICE@Example.com ", "bob@example.com", "bob@example.com"],
        "created_at": ["2026-01-01", "2026-02-15", "2026-02-15"]
    }
    df = pd.DataFrame(messy_data)
    print("=== Raw Messy Data ===")
    print(df)

    cleaned_df = clean_raw_user_dataset(df)
    print("\n=== Cleaned Data ===")
    print(cleaned_df)
