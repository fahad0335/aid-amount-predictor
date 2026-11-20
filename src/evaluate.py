# Name: Shah Fahad  Roll no: TRN-2026-000706  Date: 19-11-2026
# Purpose: best model error analysis, residual plot, and save pipeline.
import joblib
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

from src.model_data import load_model_data, time_split, TARGET
from src.pipeline import build_pipeline

MODEL_PATH = "outputs/models/aid_amount_pipeline.joblib"
REPORTS = "outputs/reports/"
FIGURES = "outputs/figures/"


def main():
    data = load_model_data()
    X_train, X_test, y_train, y_test = time_split(data)

    pipe = build_pipeline(RandomForestRegressor(n_estimators=100, min_samples_leaf=3,
                                                random_state=42, n_jobs=-1))
    pipe.fit(X_train, y_train)
    pred = pipe.predict(X_test)
    residual = y_test - pred  # positive = under-prediction, negative = over-prediction

    # 1. Residual plot
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.scatter(pred, residual, s=10, alpha=0.4, color="#2563EB")
    ax.axhline(0, color="#1E293B", linewidth=1)
    ax.set_title("Residuals: where the model is wrong", loc="left", fontweight="bold")
    ax.set_xlabel("Predicted amount (log10 of US dollars)")
    ax.set_ylabel("Actual minus predicted (log10 units)")
    fig.tight_layout()
    fig.savefig(FIGURES + "chart4_residuals.png", dpi=150)
    plt.close(fig)

    # 2. Subgroup performance
    test = data.loc[X_test.index].copy()
    test["abs_error"] = residual.abs()
    for col in ["assistance_category_name", "aid_type_group_name", "fiscal_year"]:
        out = test.groupby(col)["abs_error"].agg(["count", "mean"]).round(3)
        out.to_csv(REPORTS + f"error_by_{col}.csv")
        print(f"\nMAE (log10) by {col}:")
        print(out)

    # 3. Worst 10 rows
    test["predicted_amount"] = (10 ** pred).round(0)
    worst = test.sort_values("abs_error", ascending=False).head(10)
    cols = ["fiscal_year", "aid_type_group_name", "dac_sector_name",
            TARGET, "predicted_amount", "abs_error"]
    worst[cols].to_csv(REPORTS + "worst_10_predictions.csv", index=False)
    print("\nWorst 10 predictions:")
    print(worst[cols].to_string(index=False))

    # 4. Pipeline save
    joblib.dump(pipe, MODEL_PATH)
    print("\nSaved:", MODEL_PATH)


if __name__ == "__main__":
    main()
