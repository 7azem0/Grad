"""Simple benchmark predictors."""
from sklearn.dummy import DummyRegressor


def make_median_baseline() -> DummyRegressor:
    """Return a baseline that predicts the training-target median for every row."""
    return DummyRegressor(strategy="median")
