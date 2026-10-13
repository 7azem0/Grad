import pandas as pd
import pytest

from f1_strategy.data.prepare_laps import add_lap_time_seconds, validate_columns


def test_add_lap_time_seconds_converts_timedelta():
    frame = pd.DataFrame({"LapTime": pd.to_timedelta(["0 days 00:01:30", "0 days 00:01:32.5"])})
    result = add_lap_time_seconds(frame)
    assert result["LapTimeSeconds"].tolist() == [90.0, 92.5]
    assert "LapTimeSeconds" not in frame.columns  # original was not mutated


def test_validate_columns_reports_missing_column():
    with pytest.raises(ValueError, match="missing"):
        validate_columns(pd.DataFrame({"A": [1]}), ["A", "B"])
