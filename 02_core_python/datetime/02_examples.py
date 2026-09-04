"""
Topic: Parsing ISO String Timestamps
File: 02_examples.py
"""
from datetime import datetime

def parse_iso_timestamps() -> None:
    iso_string = "2026-09-04T14:30:00+00:00"
    
    # Python 3.7+ built-in ISO parsing
    parsed_dt = datetime.fromisoformat(iso_string)
    print(f"Parsed ISO datetime: {parsed_dt}")
    print(f"Year: {parsed_dt.year}, Month: {parsed_dt.month}, Day: {parsed_dt.day}")


if __name__ == "__main__":
    parse_iso_timestamps()
