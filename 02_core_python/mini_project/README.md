# Mini-Project 02: Automated Log & Data Processor Engine

## Project Overview
Build a high-performance, streaming log and data processor engine that ingests log files, applies filtering pipeline stages using generators and regular expressions, extracts error metrics, and generates a structured summary report in JSON and CSV formats.

## Features
1. **Streaming Log Reader**: Uses generator expressions to stream log files line-by-line without loading entire files into memory.
2. **Regex Log Parser**: Uses named regex groups `(?P<timestamp>...)`, `(?P<level>...)`, `(?P<ip>...)`, `(?P<message>...)` to parse raw log strings into structured records.
3. **Pipeline Filtering**: Filters logs by level (`ERROR`, `WARN`, `INFO`) or date range using functional generators.
4. **Export Formats**: Writes aggregated metrics into JSON and CSV summary reports using `pathlib` and context managers.

## How to Run
```bash
python 02_core_python/mini_project/main.py
```
