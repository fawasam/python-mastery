"""
ETL Pipeline Main Entrypoint.
"""

from app.pipeline import ETLPipeline


def main() -> None:
    raw_df = ETLPipeline.extract_raw_records()
    transformed_df = ETLPipeline.transform_data(raw_df)
    print("=== Transformed ETL Dataset ===")
    print(transformed_df)


if __name__ == "__main__":
    main()
