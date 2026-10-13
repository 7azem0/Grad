import pandas as pd
from unittest.mock import Mock, patch

from f1_strategy.data.fastf1_loader import load_race_laps


# 1. Create a tiny fake lap table.
fake_laps = pd.DataFrame({
    "Driver": ["VER", "HAM"],
    "LapNumber": [1, 1],
})

# 2. Create a fake session.
fake_session = Mock()
fake_session.laps = fake_laps

# 3. Replace FastF1's session lookup with our fake session.
with patch(
    "f1_strategy.data.fastf1_loader.fastf1.get_session",
    return_value=fake_session,
) as mocked_get_session:

    result = load_race_laps(2023, "Bahrain")

# 4. Check the returned data.
assert len(result) == 2
assert result["Year"].tolist() == [2023, 2023]
assert result["Event"].tolist() == ["Bahrain", "Bahrain"]

# 5. Check that the original table was not modified.
assert "Year" not in fake_laps.columns
assert "Event" not in fake_laps.columns

# 6. Check that the correct session was requested.
mocked_get_session.assert_called_once_with(2023, "Bahrain", "R")

print("All load_race_laps checks passed!")