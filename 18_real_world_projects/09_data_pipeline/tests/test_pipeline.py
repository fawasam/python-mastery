"""
Tests for ETL Data Pipeline.
"""

from app.pipeline import ETLPipeline


def test_etl_transform() -> None:
    raw = ETLPipeline.extract_raw_records()
    transformed = ETLPipeline.transform_data(raw)
    
    assert len(transformed) == 3  # Deduplicated user_id 2
    assert transformed["amount_vat"].iloc[0] == 120.0
