# Mini-Project 02 — Solution Explanation

## Architecture Overview
The Automated Log & Data Processor Engine combines Core Python functional primitives:

1. **Lazy Streaming Pipeline**:
   - `stream_log_lines()` -> `parse_log_records()` -> `filter_by_level()`.
   - Uses generator expressions so data is processed element-by-element without loading gigabytes of raw logs into RAM.

2. **Regex Pattern Extraction**:
   - Uses compiled regex `LOG_REGEX` with named capturing groups `(?P<timestamp>...)`, `(?P<level>...)`, `(?P<ip>...)`, and `(?P<message>...)`.
   - Returns structured dictionaries with datetime conversion (`datetime.fromisoformat`).

3. **Multi-Format Exporters**:
   - Outputs JSON reports using `json.dump(indent=2)`.
   - Outputs CSV summaries using `csv.DictWriter(newline="")`.

## Testing & Verification
Execute the processor main script:
```bash
python 02_core_python/mini_project/main.py
```
