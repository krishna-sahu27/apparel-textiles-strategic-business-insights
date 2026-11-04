"""Validation and cleaning helpers."""
import pandas as pd

def clean_business_data(df: pd.DataFrame) -> pd.DataFrame:
    required = {"month","category","channel","gross_units","returned_units","net_sales_inr","cost_of_goods_sold_inr","marketing_spend_inr"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")
    out = df.copy()
    out["month"] = pd.to_datetime(out["month"], errors="coerce")
    for col in ["gross_units","returned_units","net_sales_inr","cost_of_goods_sold_inr","marketing_spend_inr","discount_rate"]:
        if col in out:
            out[col] = pd.to_numeric(out[col], errors="coerce")
    out = out.drop_duplicates().dropna(subset=["month","category","channel","gross_units","net_sales_inr"])
    out = out[(out["gross_units"] >= 0) & (out["returned_units"] >= 0) & (out["returned_units"] <= out["gross_units"])]
    out["gross_margin_inr"] = out["net_sales_inr"] - out["cost_of_goods_sold_inr"]
    out["gross_margin_pct"] = out["gross_margin_inr"] / out["net_sales_inr"].replace(0, pd.NA)
    out["return_rate"] = out["returned_units"] / out["gross_units"].replace(0, pd.NA)
    return out.sort_values(["month","category","channel"]).reset_index(drop=True)
