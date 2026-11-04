"""Seasonal-naive baseline forecast with chronological holdout."""
import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error

def forecast_monthly(monthly: pd.DataFrame, horizon: int = 3):
    series = monthly.set_index("month")["net_sales_inr"].asfreq("MS").astype(float)
    if series.isna().any():
        series = series.interpolate(limit_direction="both")
    if len(series) < 15:
        raise ValueError("At least 15 monthly observations are recommended.")
    train, test = series.iloc[:-6], series.iloc[-6:]
    if len(train) >= 12:
        test_pred = pd.Series([train.iloc[-12 + i] for i in range(6)], index=test.index)
    else:
        test_pred = pd.Series([train.tail(3).mean()] * len(test), index=test.index)
    mae = mean_absolute_error(test, test_pred)
    wape = np.abs(test - test_pred).sum() / np.abs(test).sum()
    future_idx = pd.date_range(series.index[-1] + pd.offsets.MonthBegin(1), periods=horizon, freq="MS")
    future = []
    for dt in future_idx:
        prior = dt - pd.DateOffset(years=1)
        future.append(float(series.loc[prior]) if prior in series.index else float(series.tail(3).mean()))
    result = pd.DataFrame({"month": future_idx, "forecast_net_sales_inr": future})
    metrics = {"holdout_mae_inr": float(mae), "holdout_wape": float(wape), "holdout_months": len(test)}
    return result, metrics, pd.DataFrame({"actual":test, "baseline_prediction":test_pred})
