"""
Resilient Data Ingestion & Fault Telemetry Engine.
"""

import json
import logging
import sys
from typing import Any

# Configure application logging
logger = logging.getLogger("IngestionEngine")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(logging.Formatter("[%(levelname)s] %(asctime)s - %(message)s"))
if not logger.handlers:
    logger.addHandler(handler)


# 1. CUSTOM EXCEPTION HIERARCHY
class IngestionError(Exception):
    """Base exception for data ingestion failures."""

    pass


class InvalidPayloadError(IngestionError):
    """Raised when incoming JSON payload fails schema validation."""

    pass


class TargetUnavailableError(IngestionError):
    """Raised when destination database or queue is unreachable."""

    pass


# 2. DEFENSIVE VALIDATION & GUARD CLAUSES
def validate_payload(raw_data: str) -> dict[str, Any]:
    if not raw_data or not raw_data.strip():
        raise InvalidPayloadError("Received empty payload string")

    try:
        data = json.loads(raw_data)
    except json.JSONDecodeError as err:
        raise InvalidPayloadError("Malformed JSON input string") from err

    if not isinstance(data, dict):
        raise InvalidPayloadError(f"Expected JSON object dictionary, got {type(data).__name__}")

    if "sensor_id" not in data or "reading" not in data:
        raise InvalidPayloadError("Payload missing required fields 'sensor_id' or 'reading'")

    return data


# 3. FAULT-TOLERANT PROCESSING PIPELINE
def process_sensor_stream(payload_batch: list[str]) -> list[dict[str, Any]]:
    # Invariant assertion
    assert isinstance(payload_batch, list), "Payload batch must be a list"

    processed_records: list[dict[str, Any]] = []

    for idx, raw_item in enumerate(payload_batch):
        logger.info("Processing batch item %d of %d", idx + 1, len(payload_batch))
        try:
            record = validate_payload(raw_item)
            processed_records.append(record)
        except InvalidPayloadError as err:
            # Graceful recovery: log fault telemetry with exception details and continue batch
            logger.error("Skipping corrupt payload item %d: %s (Root cause: %s)", idx + 1, err, err.__cause__)

    return processed_records


if __name__ == "__main__":
    sample_batch = [
        '{"sensor_id": "SN-001", "reading": 23.5}',  # Valid
        '{"sensor_id": "SN-002"}',  # Invalid: Missing reading
        "NOT_VALID_JSON",  # Invalid: Malformed JSON
        '{"sensor_id": "SN-003", "reading": 41.2}',  # Valid
    ]

    results = process_sensor_stream(sample_batch)
    print(f"\nFinal Successfully Ingested Records Count: {len(results)}")
    for r in results:
        print(f" - {r}")
