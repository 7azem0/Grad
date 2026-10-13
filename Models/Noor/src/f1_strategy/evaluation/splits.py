from __future__ import annotations

import pandas as pd


def split_by_lap_number(
    data: pd.DataFrame,
    cutoff_lap: int,
    lap_column: str = "LapNumber",
) -> tuple[pd.DataFrame, pd.DataFrame]:

    if lap_column not in data:
        raise ValueError(f"Missing lap-number column: {lap_column}")
    train = data.loc[data[lap_column] <= cutoff_lap].copy()
    test = data.loc[data[lap_column] > cutoff_lap].copy()
    if train.empty or test.empty:
        raise ValueError("cutoff_lap must leave non-empty training and test sets.")
    return train, test
