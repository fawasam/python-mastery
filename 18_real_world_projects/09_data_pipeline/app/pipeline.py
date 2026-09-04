"""
ETL Pipeline Engine.
"""

import pandas as pd


class ETLPipeline:
    @staticmethod
    def extract_raw_records() -> pd.DataFrame:
        return pd.DataFrame({
            "user_id": [1, 2, 2, 3],
            "name": [" Alice ", "Bob", "Bob", "Charlie"],
            "amount": [100.0, 150.0, 150.0, 200.0]
        })

    @classmethod
    def transform_data(cls, df: pd.DataFrame) -> pd.DataFrame:
        clean = df.copy()
        clean["name"] = clean["name"].str.strip()
        clean = clean.drop_duplicates(subset=["user_id"])
        clean["amount_vat"] = clean["amount"] * 1.20
        return clean
