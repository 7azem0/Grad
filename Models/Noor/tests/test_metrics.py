import pytest
from f1_strategy.evaluation.metrics import regression_metrics


def test_regression_metrics_known_example():
    result = regression_metrics([10.0, 12.0], [11.0, 10.0])
    assert result["MAE_seconds"] == pytest.approx(1.5)
    assert result["RMSE_seconds"] == pytest.approx((2.5) ** 0.5)
    assert result["R2"] == pytest.approx(-1.5)


def test_regression_metrics_rejects_mismatched_lengths():
    with pytest.raises(ValueError, match="same length"):
        regression_metrics([1, 2], [1])
