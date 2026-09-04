"""
Advanced Data Analysis: Time Series Rolling Windows and Moving Averages.
"""

import pandas as pd


def compute_rolling_averages() -> None:
    # 7-day sales time series
    dates = pd.date_range(start="2026-01-01", periods=7, freq="D")
    sales = [100, 150, 200, 180, 220, 300, 280]
    
    df = pd.DataFrame({"sales": sales}, index=dates)

    # Calculate 3-day simple moving average (SMA)
    df["3_day_sma"] = df["sales"].rolling(window=3).mean()

    print("=== Time Series Sales & 3-Day Rolling Average ===")
    print(df)


if __name__ == "__main__":
    compute_rolling_averages()
