# Mini Project: End-to-End E-Commerce Data Pipeline

## Overview
In this mini project, you will build a complete Pandas & NumPy data processing pipeline that reads raw messy transactional records, cleans nulls and dates, calculates total customer lifetime values (LTV), and computes department analytics summaries.

## Pipeline Phases
1. **Ingestion & Cleaning**: Parse dates, trim strings, handle missing values.
2. **Feature Engineering**: Calculate total transaction value ($price \times quantity$).
3. **Aggregation & Reporting**: Group by category to compute revenue metrics.

## Running the Pipeline
```bash
python main.py
```
