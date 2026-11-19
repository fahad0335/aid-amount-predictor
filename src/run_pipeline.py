# Name: Shah Fahad  Roll no: TRN-2026-000706  Date: 19-11-2026
# Purpose: raw data -> clean -> validate -> save cleaned data + metrics.
import json
import pandas as pd
from src.cleaning import (remove_duplicates, parse_dates,
                          fill_missing_categories, flag_negative_amounts)
from src.validation import check_no_missing, check_range

RAW_PATH = "data/raw/us_aid_pakistan.csv"
CLEAN_PATH = "data/cleaned/us_aid_cleaned.csv"
METRICS_PATH = "outputs/reports/data_quality_metrics.json"
DATE_COLS = ["activity_start_date", "activity_end_date"]


def main():
    raw = pd.read_csv(RAW_PATH, low_memory=False)
    df = remove_duplicates(raw)
    df = parse_dates(df, DATE_COLS)
    df = fill_missing_categories(df, ["subagency_acronym"])
    df = flag_negative_amounts(df)

    check_no_missing(df, ["subagency_acronym", "current_amount", "fiscal_year"])
    check_range(df, "fiscal_year", 2001, 2021)

    metrics = {
        "rows_before": len(raw),
        "rows_after": len(df),
        "duplicates_removed": len(raw) - len(df),
        "missing_pct_before": raw.isna().mean().mul(100).round(1).to_dict(),
        "missing_pct_after": df.isna().mean().mul(100).round(1).to_dict(),
        "negative_amount_rows": int(df["is_negative_amount"].sum()),
    }

    df.to_csv(CLEAN_PATH, index=False)
    with open(METRICS_PATH, "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2)
    print("Done. Rows:", len(raw), "->", len(df))


if __name__ == "__main__":
    main()