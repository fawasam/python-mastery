"""
Mini-Project 02: Automated Log & Data Processor Engine
File: main.py

Demonstrates Core Python capabilities:
comprehensions, generators, regex parsing, datetime calculations,
JSON/CSV serialization, context managers, and pathlib.
"""
import csv
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Generator

LOG_REGEX = re.compile(
    r"^(?P<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z)\s+"
    r"\[(?P<level>INFO|WARN|ERROR)\]\s+"
    r"(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+-\s+"
    r"(?P<message>.+)$"
)

SAMPLE_LOGS = [
    "2026-09-04T10:00:01Z [INFO] 192.168.1.10 - User login success",
    "2026-09-04T10:00:02Z [ERROR] 192.168.1.50 - Database connection pool exhausted",
    "2026-09-04T10:00:03Z [WARN] 192.168.1.20 - High memory consumption threshold 85%",
    "2026-09-04T10:00:04Z [ERROR] 192.168.1.50 - Failed to acquire lock for user_9901",
    "2026-09-04T10:00:05Z [INFO] 192.168.1.12 - Health check status OK",
]


def stream_log_lines(lines: list[str]) -> Generator[str, None, None]:
    """Generator streaming raw log lines."""
    for line in lines:
        if line.strip():
            yield line.strip()


def parse_log_records(line_stream: Generator[str, None, None]) -> Generator[dict[str, Any], None, None]:
    """Generator parsing raw log strings into structured dictionaries via regex."""
    for line in line_stream:
        match = LOG_REGEX.match(line)
        if match:
            record = match.groupdict()
            record["dt"] = datetime.fromisoformat(record["timestamp"].replace("Z", "+00:00"))
            yield record


def filter_by_level(record_stream: Generator[dict[str, Any], None, None], target_level: str) -> Generator[dict[str, Any], None, None]:
    """Generator filtering records by level."""
    for record in record_stream:
        if record["level"] == target_level:
            yield record


def process_log_pipeline(logs: list[str]) -> dict[str, Any]:
    """Execute complete processing pipeline and aggregate metrics."""
    raw_stream = stream_log_lines(logs)
    records = list(parse_log_records(raw_stream))

    level_counts = Counter(r["level"] for r in records)
    ip_counts = Counter(r["ip"] for r in records)
    error_messages = [r["message"] for r in records if r["level"] == "ERROR"]

    metrics = {
        "processed_at": datetime.now(timezone.utc).isoformat(),
        "total_logs": len(records),
        "levels": dict(level_counts),
        "top_ips": dict(ip_counts.most_common(2)),
        "error_count": len(error_messages),
        "errors": error_messages,
    }
    return metrics


def export_reports(metrics: dict[str, Any], base_dir: Path) -> tuple[Path, Path]:
    """Export summary metrics to JSON and CSV formats."""
    json_path = base_dir / "log_summary.json"
    csv_path = base_dir / "log_summary.csv"

    # Export JSON
    with json_path.open("w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2)

    # Export CSV
    fieldnames = ["metric", "value"]
    rows = [
        {"metric": "total_logs", "value": metrics["total_logs"]},
        {"metric": "error_count", "value": metrics["error_count"]},
        {"metric": "processed_at", "value": metrics["processed_at"]},
    ]
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    return json_path, csv_path


if __name__ == "__main__":
    print("--- Running Automated Log Processor Engine ---")
    metrics = process_log_pipeline(SAMPLE_LOGS)
    print(f"Metrics Summary:\n{json.dumps(metrics, indent=2)}")

    current_dir = Path(__file__).parent
    json_out, csv_out = export_reports(metrics, current_dir)
    print(f"\n✅ Reports generated:\n  - {json_out.name}\n  - {csv_out.name}")

    if json_out.exists():
        json_out.unlink()
    if csv_out.exists():
        csv_out.unlink()
