# Data Processing Mini Project Breakdown

## Pipeline Engineering Summary
1. **Sanitation**: Standardizes whitespace and capitalization across category string fields (`.str.strip().str.capitalize()`).
2. **Median Imputation**: Replaces missing price values with median dataset price.
3. **Vectorized Math**: Computes order total sale value (`price * quantity`) using C-speed Pandas vectorization.
4. **Aggregation**: Groups by product category to calculate Total Revenue, AOV (Average Order Value), and Order Counts.
