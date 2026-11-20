# Name: Shah Fahad  Roll no: TRN-2026-000706  Date: 19-11-2026
# Purpose: cleaned data se Pandas summaries aur NumPy operations, files mein save.
import numpy as np
import pandas as pd

CLEAN_PATH = "data/cleaned/us_aid_cleaned.csv"
REPORTS = "outputs/reports/"


def main():
    df = pd.read_csv(CLEAN_PATH, low_memory=False)

    # --- Pandas ---
    by_year = df.groupby("fiscal_year")["current_amount"].agg(["count", "sum", "median"])
    by_year.to_csv(REPORTS + "summary_by_year.csv")

    year_by_type = df.pivot_table(index="fiscal_year", columns="assistance_category_name",
                                  values="current_amount", aggfunc="sum")
    year_by_type.to_csv(REPORTS + "pivot_year_by_assistance.csv")

    top_agencies = (df.groupby("implementing_agency_name")["current_amount"]
                    .sum().sort_values(ascending=False).head(10))
    top_agencies.to_csv(REPORTS + "top10_agencies.csv")

    aid_types = df["aid_type_group_name"].value_counts()
    aid_types.to_csv(REPORTS + "aid_type_counts.csv")

    # --- NumPy (vectorized, bina loop) ---
    amount = df["current_amount"].to_numpy()
    direction = np.where(amount < 0, "negative", "positive")
    log10_abs = np.log10(np.abs(amount))
    p = np.percentile(amount, [25, 50, 75, 99])

    print(by_year.head())
    print(top_agencies)
    print(aid_types)
    print(pd.Series(direction).value_counts())
    print("log10 of |amount|: min", log10_abs.min().round(2), "max", log10_abs.max().round(2))
    print("percentiles 25/50/75/99:", p)


if __name__ == "__main__":
    main()
