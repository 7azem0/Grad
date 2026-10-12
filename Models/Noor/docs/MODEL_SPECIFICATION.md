# Initial lap-time model specification

## Target

For a lap \(i\), the target is \(y_i\), the recorded duration of the lap in seconds (`LapTimeSeconds`).

## Initial predictors

- `Driver`: categorical driver identifier.
- `Compound`: categorical tyre-compound label.
- `TyreLife`: numeric tyre-age field from FastF1.

These are candidate predictors only. Before claiming live prediction capability, verify that each field's value is known at the intended prediction timestamp. In particular, confirm the exact semantics/timing of `TyreLife`.

## Linear regression

The least-squares model estimates coefficients that minimize residual sum of squares:

\[
\widehat y_i = \beta_0 + \sum_{j=1}^{p}\beta_j x_{ij}
\]

\[
RSS = \sum_{i=1}^{n}(y_i-\widehat y_i)^2
\]

Categorical variables are one-hot encoded; the numeric tyre-age field is passed through. The coefficient estimates describe fitted associations conditional on the other encoded inputs; they do not establish causality.

## Metrics

\[
MAE=\frac{1}{n}\sum_{i=1}^{n}|y_i-\widehat y_i|
\]

MAE is the average absolute error, in seconds.

\[
RMSE=\sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_i-\widehat y_i)^2}
\]

RMSE is also in seconds and gives larger errors more influence.

\[
R^2=1-\frac{\sum_i(y_i-\widehat y_i)^2}{\sum_i(y_i-\bar y)^2}
\]

R² is relative to predicting the evaluation-set mean. It can be negative. The median baseline predicts the training median, so it does not necessarily achieve R²=0.

## Current evidence and limitations

The reported experiments found:
- Held-out Silverstone: linear regression MAE 9.958 s, RMSE 11.427 s, R² -118.965; median baseline MAE 1.043 s, RMSE 1.305 s, R² -0.564.
- Bahrain laps 41–57 test: linear regression MAE 1.860 s, RMSE 2.166 s, R² -5.139; median baseline MAE 1.307 s, RMSE 1.461 s, R² -1.793.

These are the user's recorded experiment results, not regenerated results from this refactored package. The linear model loses to the baseline on both experiments. The first split tests a different circuit, and the second tests later laps within the same race. Neither alone establishes generalization to all circuits/seasons.

## Leakage and data-quality cautions

- Avoid predictors that are measured during or after the target lap if the intended prediction is made before that lap.
- `TrackStatus` attached to a completed lap can contain status codes that occurred during that lap; it must not be used as a start-of-lap feature without time alignment.
- `IsAccurate=True` and `Deleted=False` is a provisional filter, not a complete pit-lap or race-control policy.
- Do not delete slow laps just because they are outliers; inspect context and define rules before filtering.
