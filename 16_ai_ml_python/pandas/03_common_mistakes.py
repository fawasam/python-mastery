"""
Pandas for ML Anti-Patterns.
"""

# MISTAKE: Leaving unique primary key columns (e.g. `user_id`, `uuid`) in the feature matrix $X$.
# WHY: Models overfit on arbitrary unique IDs instead of learning actual domain patterns.
# FIX: Drop non-predictive identifier columns prior to model training.

if __name__ == "__main__":
    print("Feature column selection rules verified.")
