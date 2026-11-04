"""Exploratory summaries."""
import pandas as pd

def create_eda_tables(df: pd.DataFrame):
    monthly = df.groupby("month", as_index=False).agg(net_sales_inr=("net_sales_inr","sum"), units=("gross_units","sum"), gross_margin_inr=("gross_margin_inr","sum"), returned_units=("returned_units","sum"))
    monthly["gross_margin_pct"] = monthly["gross_margin_inr"] / monthly["net_sales_inr"]
    monthly["return_rate"] = monthly["returned_units"] / monthly["units"]
    category = df.groupby("category", as_index=False).agg(net_sales_inr=("net_sales_inr","sum"), gross_margin_inr=("gross_margin_inr","sum"), units=("gross_units","sum"))
    category["gross_margin_pct"] = category["gross_margin_inr"] / category["net_sales_inr"]
    channel = df.groupby("channel", as_index=False).agg(net_sales_inr=("net_sales_inr","sum"), marketing_spend_inr=("marketing_spend_inr","sum"), gross_margin_inr=("gross_margin_inr","sum"))
    channel["margin_after_marketing_inr"] = channel["gross_margin_inr"] - channel["marketing_spend_inr"]
    return monthly, category, channel
