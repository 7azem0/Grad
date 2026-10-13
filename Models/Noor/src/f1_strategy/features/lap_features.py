from __future__ import annotations

import pandas as pd

CATEGORICAL_FEATURES = ["Driver", "Compound"]
NUMERIC_FEATURES = ["TyreLife"]
FEATURES = CATEGORICAL_FEATURES + NUMERIC_FEATURES
TARGET = "LapTimeSeconds"


def select_model_columns(data: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    required = FEATURES + [TARGET]
    missing = sorted(set(required) - set(data.columns))
    if missing:
        raise ValueError(f"Model columns are missing: {missing}")
    subset = data.loc[:, required].dropna().copy()
    X = subset[FEATURES]
    y = subset[TARGET]
    return X, y
