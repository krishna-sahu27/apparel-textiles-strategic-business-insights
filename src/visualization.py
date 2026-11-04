"""Save business charts."""
from pathlib import Path
import matplotlib.pyplot as plt

def save_charts(monthly, category, forecast, out_dir):
    out = Path(out_dir); out.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(10,5)); ax.plot(monthly["month"], monthly["net_sales_inr"])
    ax.set(title="Monthly Net Sales — Synthetic", xlabel="Month", ylabel="Net sales (INR)")
    fig.tight_layout(); fig.savefig(out / "monthly_net_sales.png", dpi=160); plt.close(fig)
    fig, ax = plt.subplots(figsize=(8,5)); ax.bar(category["category"], category["net_sales_inr"])
    ax.set(title="Net Sales by Category — Synthetic", xlabel="Category", ylabel="Net sales (INR)"); ax.tick_params(axis="x", rotation=20)
    fig.tight_layout(); fig.savefig(out / "category_sales.png", dpi=160); plt.close(fig)
    fig, ax = plt.subplots(figsize=(9,5)); ax.plot(forecast["month"], forecast["forecast_net_sales_inr"], marker="o")
    ax.set(title="Three-Month Baseline Forecast — Synthetic", xlabel="Month", ylabel="Forecast net sales (INR)")
    fig.tight_layout(); fig.savefig(out / "sales_forecast.png", dpi=160); plt.close(fig)
