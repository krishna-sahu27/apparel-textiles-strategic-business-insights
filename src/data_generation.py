"""Generate deterministic synthetic monthly apparel data (fictional only)."""
from pathlib import Path
import numpy as np
import pandas as pd
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DATA.mkdir(exist_ok=True)

def build_data():
    rng = np.random.default_rng(27)
    months = pd.date_range("2023-01-01", periods=36, freq="MS")
    categories = ["Casualwear", "Ethnicwear", "Formalwear", "Sportswear"]
    channels = ["Online", "Retail Store"]
    base = {"Casualwear": 950, "Ethnicwear": 700, "Formalwear": 520, "Sportswear": 600}
    price = {"Casualwear": 950, "Ethnicwear": 1250, "Formalwear": 1500, "Sportswear": 1100}
    ratio = {"Casualwear": .52, "Ethnicwear": .55, "Formalwear": .50, "Sportswear": .48}
    rows = []
    for i, month in enumerate(months):
        season = 1 + .16 * np.sin(2 * np.pi * (month.month - 1) / 12)
        festival = 1.18 if month.month in (10, 11) else 1.0
        growth = 1 + .006 * i
        for cat in categories:
            for channel in channels:
                units = max(30, int(base[cat] * season * festival * growth * (1.08 if channel == "Online" else .92) * rng.normal(1, .07)))
                avg_price = price[cat] * rng.normal(1, .025)
                discount = rng.uniform(.04, .16)
                gross = units * avg_price
                returns = int(units * rng.uniform(.025, .085))
                net = gross * (1 - discount) * ((units - returns) / units)
                cogs = net * ratio[cat]
                marketing = net * (.045 if channel == "Online" else .025) * rng.uniform(.8, 1.2)
                rows.append([month.date().isoformat(),cat,channel,units,returns,round(avg_price,2),round(discount,4),round(net,2),round(cogs,2),round(marketing,2)])
    cols = ["month","category","channel","gross_units","returned_units","average_list_price_inr","discount_rate","net_sales_inr","cost_of_goods_sold_inr","marketing_spend_inr"]
    df = pd.DataFrame(rows, columns=cols)
    df.to_csv(DATA / "synthetic_monthly_business_data.csv", index=False)
    return df
if __name__ == "__main__":
    print(build_data().head().to_string(index=False))
