from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def regression_metrics(actual, predicted) -> dict[str, float]:
    actual = np.asarray(actual, dtype=float)
    predicted = np.asarray(predicted, dtype=float)
    if actual.ndim != 1 or predicted.ndim != 1:
        raise ValueError("actual and predicted must be one-dimensional.")
    if len(actual) != len(predicted):
        raise ValueError("actual and predicted must have the same length.")
    if len(actual) == 0:
        raise ValueError("Cannot evaluate empty arrays.")
    if not np.isfinite(actual).all() or not np.isfinite(predicted).all():
        raise ValueError("actual and predicted must contain only finite values.")
    return {
        "MAE_seconds": float(mean_absolute_error(actual, predicted)),
        "RMSE_seconds": float(np.sqrt(mean_squared_error(actual, predicted))),
        "R2": float(r2_score(actual, predicted)),
    }


def compare_predictions(actual, predictions: dict[str, np.ndarray]) -> pd.DataFrame:
    """Evaluate multiple named prediction arrays using identical actual rows."""
    rows = {
        name: regression_metrics(actual, values)
        for name, values in predictions.items()
    }
    return pd.DataFrame.from_dict(rows, orient="index")
