# Data Transformation & Feature Engineering

## What You Will Learn
- One-hot encoding categorical variables (`pd.get_dummies()`)
- Binning continuous values into discrete intervals (`pd.cut()`)
- Custom row/column transformations with `.apply()` and `.map()`
- Reshaping DataFrames with `.pivot_table()` and `.melt()`

## Why This Matters
Raw datasets are rarely in the exact format required by machine learning models or analytical reporting dashboards. Data transformation reshapes, normalizes, and encodes raw columns into structured numerical feature sets.

## Core Transformations
1. **One-Hot Encoding**: Converting string categories into binary indicator columns ($0$ or $1$).
2. **Feature Binning**: Discretizing continuous ages or incomes into generational or tax bracket categories.

## Examples
See `01_basic.py` and `02_examples.py` for runnable code.

## Exercises
Complete exercises in `04_exercises.py` and check `05_solution.py`.

## Next Topic
Proceed to `../data_analysis/`.
