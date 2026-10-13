from __future__ import annotations

import pandas as pd

REQUIRED_RAW_COLUMNS = ["Driver", "LapTime", "Compound", "TyreLife", "LapNumber"]
QUALITY_COLUMNS = ["IsAccurate", "Deleted"]


def validate_columns(data: pd.DataFrame, required: list[str]) -> None:
    missing = sorted(set(required) - set(data.columns))
    if missing:
        raise ValueError(f"Required columns are missing: {missing}")


def add_lap_time_seconds(data: pd.DataFrame) -> pd.DataFrame:
    validate_columns(data, ["LapTime"])
    result = data.copy()
    result["LapTimeSeconds"] = pd.to_timedelta(result["LapTime"]).dt.total_seconds()
    return result


def make_candidate_laps(data: pd.DataFrame) -> pd.DataFrame:
    """Create the notebook's provisional modelling subset.

    Rule: keep rows with a recorded lap time, IsAccurate=True, and Deleted=False.
    This rule is intentionally explicit but is not a universal definition of a
    valid racing lap. Pit-in/out and race-control effects require separate review.
    """
    validate_columns(data, REQUIRED_RAW_COLUMNS + QUALITY_COLUMNS)
    result = add_lap_time_seconds(data)
    keep = (
        result["LapTimeSeconds"].notna()
        & result["IsAccurate"].eq(True)
        & result["Deleted"].eq(False)
    )
    return result.loc[keep].copy()
