"""Run the complete Week 6 synthetic analytics workflow."""
from pathlib import Path
import pandas as pd
from data_generation import build_data
from data_cleaning import clean_business_data
from eda import create_eda_tables
from forecasting import forecast_monthly
from visualization import save_charts
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output"

def main():
    raw = build_data(); clean = clean_business_data(raw)
    monthly, category, channel = create_eda_tables(clean)
    forecast, metrics, holdout = forecast_monthly(monthly)
    OUT.mkdir(exist_ok=True)
    clean.to_csv(OUT / "cleaned_integrated_data.csv", index=False)
    monthly.to_csv(OUT / "monthly_kpis.csv", index=False)
    category.to_csv(OUT / "category_summary.csv", index=False)
    channel.to_csv(OUT / "channel_summary.csv", index=False)
    forecast.to_csv(OUT / "three_month_forecast.csv", index=False)
    holdout.to_csv(OUT / "forecast_holdout.csv")
    pd.Series(metrics).to_json(OUT / "forecast_metrics.json", indent=2)
    save_charts(monthly, category, forecast, OUT / "charts")
    print("Analysis completed. Outputs saved to", OUT)
    print("Forecast metrics:", metrics)
    print("Category summary:\n", category.to_string(index=False))
    print("Channel summary:\n", channel.to_string(index=False))
if __name__ == "__main__":
    main()
