from __future__ import annotations

import pandas as pd
import fastf1


def load_race_laps(year: int, event: str, session_code: str = "R") -> pd.DataFrame:
    session = fastf1.get_session(year, event, session_code)
    session.load(laps=True, telemetry=False, weather=False, messages=True)
    laps = session.laps.copy()
    if laps.empty:
        raise ValueError(f"No lap rows returned for {year} {event} {session_code}.")
    laps["Year"] = year
    laps["Event"] = event
    return laps


def load_races(races: list[tuple[int, str]], session_code: str = "R") -> pd.DataFrame:
    if not races:
        raise ValueError("races must contain at least one (year, event) pair.")
    frames = [load_race_laps(year, event, session_code) for year, event in races]
    return pd.concat(frames, ignore_index=True, sort=False)
