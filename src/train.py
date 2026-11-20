# Name: Shah Fahad  Roll no: TRN-2026-000706  Date: 20-11-2026
# Purpose: baseline and comparison of 2 candidate models on the same split.
import numpy as np
import pandas as pd
from sklearn.dummy import DummyRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import TimeSeriesSplit, cross_val_score

from src.model_data import load_model_data, time_split
from src.pipeline import build_pipeline

RESULTS_PATH = "outputs/reports/model_comparison.csv"

MODELS = {
    "Baseline (median)": DummyRegressor(strategy="median"),
    "Ridge": Ridge(alpha=1.0),
    "Random Forest": RandomForestRegressor(n_estimators=100, min_samples_leaf=3,
                                           random_state=42, n_jobs=-1),
}


def main():
    X_train, X_test, y_train, y_test = time_split(load_model_data())

    # Cross-validation ke liye train ko saal ke hisaab se sort karo
    order = X_train["fiscal_year"].argsort(kind="stable")
    X_cv, y_cv = X_train.iloc[order], y_train.iloc[order]
    cv = TimeSeriesSplit(n_splits=5)

    rows = []
    for name, model in MODELS.items():
        pipe = build_pipeline(model)

        cv_mae = -cross_val_score(pipe, X_cv, y_cv, cv=cv,
                                  scoring="neg_mean_absolute_error").mean()

        pipe.fit(X_train, y_train)          # fit sirf train par
        pred = pipe.predict(X_test)         # test sirf aakhir mein

        rows.append({
            "model": name,
            "cv_mae_log10": round(cv_mae, 3),
            "test_mae_log10": round(mean_absolute_error(y_test, pred), 3),
            "test_rmse_log10": round(np.sqrt(mean_squared_error(y_test, pred)), 3),
            "test_r2": round(r2_score(y_test, pred), 3),
            "test_typical_error_factor": round(10 ** mean_absolute_error(y_test, pred), 1),
        })

    results = pd.DataFrame(rows)
    results.to_csv(RESULTS_PATH, index=False)
    print(results.to_string(index=False))


if __name__ == "__main__":
    main()