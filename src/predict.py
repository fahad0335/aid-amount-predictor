# Name: ...  Roll no: ...  Date: ...
# Purpose: save predictions to a CSV file.
# Use: python -m src.predict data/new_rows_sample.csv outputs/predictions.csv
import sys
import joblib
import pandas as pd

from src.model_data import FEATURES

MODEL_PATH = "outputs/models/aid_amount_pipeline.joblib"


def validate_columns(df):
    """Raise ValueError if any required feature column is missing."""
    missing = [col for col in FEATURES if col not in df.columns]
    if missing:
        raise ValueError(f"Input file is missing columns: {missing}")


def main():
    if len(sys.argv) != 3:
        print("Usage: python -m src.predict <input.csv> <output.csv>")
        sys.exit(1)
    input_path, output_path = sys.argv[1], sys.argv[2]

    df = pd.read_csv(input_path)
    validate_columns(df)

    pipe = joblib.load(MODEL_PATH)
    log_pred = pipe.predict(df[FEATURES])

    df["predicted_amount_usd"] = (10 ** log_pred).round(0)
    df.to_csv(output_path, index=False)
    print(df[["fiscal_year", "aid_type_group_name", "predicted_amount_usd"]].to_string(index=False))
    print("Saved:", output_path)


if __name__ == "__main__":
    main()