# Data dictionary (initial fields)

| Field | Meaning in this project | Type / unit | Notes |
|---|---|---|---|
| `Year` | Championship season identifier added by our loader | integer | Source metadata |
| `Event` | Event name added by our loader | category | Current experiments use Bahrain, Monaco, Silverstone |
| `Driver` | FastF1 driver abbreviation | category | Driver coverage may differ across races |
| `LapNumber` | Lap index from the session lap table | numeric / lap count | Used for chronological splits |
| `LapTime` | Recorded lap duration | pandas Timedelta | Convert to seconds for modelling |
| `LapTimeSeconds` | Derived lap duration | seconds | Current target |
| `Compound` | Tyre compound label | category | Inspect missing/unknown labels |
| `TyreLife` | FastF1 tyre-age field | numeric / laps | Confirm timing semantics before live use |
| `IsAccurate` | FastF1 accuracy flag | boolean-like | Meaning and missing values must be respected |
| `Deleted` | FastF1 deleted-lap flag | boolean-like | A provisional exclusion condition |
| `TrackStatus` | Lap-level track-status codes | encoded string | May reflect events during the lap; not automatically prediction-time safe |
| `PitInTime` | Pit-entry timing field | time-like | Useful for identifying pit-entry context |
| `PitOutTime` | Pit-exit timing field | time-like | Useful for identifying pit-exit context |
| `DeletedReason` | Recorded reason for deletion when available | text/category | May be missing |

Always inspect the columns and missingness in the loaded data. This dictionary documents the initial workflow, not a guarantee that every field exists for every event.
