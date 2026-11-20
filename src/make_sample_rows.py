# Name: Shah Fahad  Roll no: TRN-2026-000706  Date: 20-11-2026
# Purpose: small sample of new (unseen) rows.
import pandas as pd
from src.model_data import load_model_data, time_split, FEATURES

OUT_PATH = "data/new_rows_sample.csv"


def main():
    _, X_test, _, _ = time_split(load_model_data())
    X_test.sample(5, random_state=1)[FEATURES].to_csv(OUT_PATH, index=False)
    print("Saved:", OUT_PATH)


if __name__ == "__main__":
    main()