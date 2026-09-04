# Mini Project: High-Performance Data Processing Pipeline & Benchmarking Suite

## Overview
In this mini project, you will build a performance benchmarking and profiling suite that takes an inefficient data processing pipeline ($O(n^2)$ search, un-cached calculations, naive string manipulation) and optimizes it using proper algorithmic choices, LRU caching, and slot optimizations.

## Objectives
1. Profile an inefficient log aggregation task.
2. Measure CPU execution time and memory footprint before and after optimization.
3. Apply standard performance techniques: `__slots__`, `functools.lru_cache`, hash sets for $O(1)$ lookups, and generator expressions.

## Project Structure
- `main.py`: Interactive script comparing the Naive vs Optimized pipeline performance.
- `solution_explanation.md`: Architectural breakdown of the speedups achieved.

## Running the Project
```bash
python main.py
```
