# Data Cleaning & Sanitation Pipelines

## What You Will Learn
- Cleaning dirty text fields (whitespace trimming, case normalization)
- Standardizing date and timestamp formats
- Detecting and removing duplicate rows
- Imputing or handling missing/null values safely

## Why This Matters
"Garbage in, garbage out." Real-world data is notoriously messy. Raw CSV files contain trailing spaces, inconsistent date strings, duplicate entries, and corrupted missing values.

## Core Cleaning Operations
1. **Deduplication**: Removing identical rows using `.drop_duplicates()`.
2. **DataType Conversion**: Converting strings to numeric or datetime objects using `pd.to_datetime()`.
3. **Outlier Filtering**: Detecting numerical anomalies using IQR or Z-score bounds.

## Examples
See `01_basic.py` and `02_examples.py` for runnable code.

## Exercises
Complete exercises in `04_exercises.py` and verify in `05_solution.py`.

## Next Topic
Proceed to `../data_transformation/`.
