from __future__ import annotations

import importlib.util
from pathlib import Path

import pandas as pd
import pytest


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "python" / "bdi_analysis.py"
SPEC = importlib.util.spec_from_file_location("bdi_analysis", MODULE_PATH)
assert SPEC and SPEC.loader
bdi_analysis = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(bdi_analysis)


def test_load_data_cleans_prices_and_sorts_dates(tmp_path: Path) -> None:
    source = tmp_path / "bdi.csv"
    pd.DataFrame(
        {
            "Date": ["03/01/2024", "invalid", "01/01/2024"],
            "Price": ["2,100.00", "1,900.00", "1,800.00"],
        }
    ).to_csv(source, index=False)

    result = bdi_analysis.load_data(source)

    assert result["Date"].dt.strftime("%Y-%m-%d").tolist() == [
        "2024-01-01",
        "2024-03-01",
    ]
    assert result["Price"].tolist() == [1800, 2100]


def test_load_data_rejects_missing_columns(tmp_path: Path) -> None:
    source = tmp_path / "bdi.csv"
    pd.DataFrame({"Date": ["01/01/2024"], "Close": [1800]}).to_csv(
        source, index=False
    )

    with pytest.raises(ValueError, match="Missing required columns"):
        bdi_analysis.load_data(source)


def test_add_metrics_calculates_returns_averages_and_drawdown() -> None:
    frame = pd.DataFrame(
        {
            "Date": pd.date_range("2024-01-01", periods=4, freq="MS"),
            "Price": [1000, 1100, 1200, 900],
        }
    )

    result = bdi_analysis.add_metrics(frame)

    assert result.loc[1, "MoM"] == pytest.approx(0.10)
    assert result.loc[2, "MA_3M"] == pytest.approx(1100)
    assert result.loc[3, "Drawdown"] == pytest.approx(-0.25)
    assert result["Year"].tolist() == [2024, 2024, 2024, 2024]


def test_annual_summary_reports_yearly_observations() -> None:
    frame = pd.DataFrame(
        {
            "Date": pd.to_datetime(["2023-12-01", "2024-01-01", "2024-02-01"]),
            "Price": [1000, 1200, 1800],
        }
    )
    metrics = bdi_analysis.add_metrics(frame)

    result = bdi_analysis.annual_summary(metrics)

    assert result["Year"].tolist() == [2023, 2024]
    assert result["Observations"].tolist() == [1, 2]
    average_2024 = result.loc[result["Year"] == 2024, "Average_BDI"].item()
    assert average_2024 == pytest.approx(1500)
