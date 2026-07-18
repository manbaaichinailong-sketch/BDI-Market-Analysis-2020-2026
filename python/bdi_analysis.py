"""Reproducible Baltic Dry Index analysis for the 2020-2026 dataset."""

from __future__ import annotations

from pathlib import Path
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "excel" / "Baltic Dry Index Historical Data.csv"
OUTPUT_DIR = ROOT / "data"
IMAGE_FILE = ROOT / "images" / "bdi_trend_python.png"


def load_data(path: Path) -> pd.DataFrame:
    """Load, validate and clean the monthly BDI source file."""
    if not path.exists():
        raise FileNotFoundError(f"Data file not found: {path}")

    df = pd.read_csv(path)
    required = {"Date", "Price"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    df["Date"] = pd.to_datetime(
        df["Date"], format="%m/%d/%Y", errors="coerce"
    )
    df["Price"] = pd.to_numeric(
        df["Price"].astype(str).str.replace(",", "", regex=False),
        errors="coerce",
    )
    df = (
        df.dropna(subset=["Date", "Price"])
        .sort_values("Date")
        .drop_duplicates(subset=["Date"], keep="last")
        .reset_index(drop=True)
    )

    if df.empty:
        raise ValueError("No valid BDI observations were found.")

    return df


def add_metrics(df: pd.DataFrame) -> pd.DataFrame:
    """Add return, trend and drawdown metrics."""
    out = df.copy()
    out["MoM"] = out["Price"].pct_change()
    out["MA_3M"] = out["Price"].rolling(3, min_periods=1).mean()
    out["MA_12M"] = out["Price"].rolling(12, min_periods=1).mean()
    out["Running_Peak"] = out["Price"].cummax()
    out["Drawdown"] = out["Price"] / out["Running_Peak"] - 1
    out["Year"] = out["Date"].dt.year
    return out


def annual_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate the monthly series into an annual market summary."""
    summary = (
        df.groupby("Year")
        .agg(
            Average_BDI=("Price", "mean"),
            Minimum=("Price", "min"),
            Maximum=("Price", "max"),
            Monthly_Volatility=("MoM", "std"),
            Worst_Drawdown=("Drawdown", "min"),
            Observations=("Price", "size"),
        )
        .reset_index()
    )
    summary["Annual_Average_YoY"] = summary["Average_BDI"].pct_change()
    return summary


def save_chart(df: pd.DataFrame, output_path: Path) -> None:
    """Create the BDI trend chart without requiring a desktop display."""
    output_path.parent.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(13, 6.5))
    plt.plot(df["Date"], df["Price"], linewidth=2, label="BDI")
    plt.plot(
        df["Date"],
        df["MA_12M"],
        linestyle="--",
        linewidth=1.8,
        label="12M moving average",
    )
    plt.title("Baltic Dry Index (BDI) Monthly Trend, 2020-2026")
    plt.xlabel("Date")
    plt.ylabel("BDI points")
    plt.grid(True, alpha=0.25)
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_path, dpi=220)
    plt.close()


def print_summary(df: pd.DataFrame) -> None:
    latest = df.iloc[-1]
    peak = df.loc[df["Price"].idxmax()]
    trough = df.loc[df["Price"].idxmin()]

    print("BDI analysis completed")
    print("-" * 60)
    print(f"Observations: {len(df)}")
    print(f"Period: {df['Date'].min().date()} to {df['Date'].max().date()}")
    print(f"Latest: {latest['Price']:,.0f}")
    print(f"Peak: {peak['Price']:,.0f} ({peak['Date'].date()})")
    print(f"Trough: {trough['Price']:,.0f} ({trough['Date'].date()})")
    print(f"Latest drawdown: {latest['Drawdown']:.1%}")


def main() -> int:
    try:
        raw = load_data(DATA_FILE)
        analysis = add_metrics(raw)
        annual = annual_summary(analysis)

        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        analysis.to_csv(
            OUTPUT_DIR / "BDI_Analysis_Output.csv",
            index=False,
            encoding="utf-8-sig",
        )
        annual.to_csv(
            OUTPUT_DIR / "BDI_Annual_Summary.csv",
            index=False,
            encoding="utf-8-sig",
        )
        save_chart(analysis, IMAGE_FILE)
        print_summary(analysis)
        return 0
    except (FileNotFoundError, ValueError, pd.errors.ParserError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
