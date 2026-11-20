# Name: Shah Fahad  Roll no: TRN-2026-000706  Date: 20-11-2026
# Purpose: Part B ke liye data tayyar karna: target, features aur time-based split.
import numpy as np
import pandas as pd

CLEAN_PATH = "data/cleaned/us_aid_cleaned.csv"
TARGET = "current_amount"
LAST_TRAIN_YEAR = 2017  # 2001-2017 train, 2018-2021 test

CATEGORICAL_FEATURES = [
    "implementing_agency_name", "subagency_name", "channel_category_name",
    "dac_category_name", "dac_sector_name", "funding_account_name",
    "assistance_category_name", "aid_type_group_name",
]
NUMERIC_FEATURES = ["fiscal_year"]
FEATURES = CATEGORICAL_FEATURES + NUMERIC_FEATURES


def load_model_data(path=CLEAN_PATH):
    """Load cleaned data and keep only rows with a positive amount.

    Negative amounts are excluded because the target is modelled on a log scale,
    and the log of a negative number does not exist.
    """
    df = pd.read_csv(path, low_memory=False)
    return df[df[TARGET] > 0].reset_index(drop=True)


def time_split(df, last_train_year=LAST_TRAIN_YEAR):
    """Split by fiscal year: years up to last_train_year train, later years test.

    Returns X_train, X_test, y_train, y_test. y is log10 of the amount.
    """
    train = df[df["fiscal_year"] <= last_train_year]
    test = df[df["fiscal_year"] > last_train_year]
    y_train = np.log10(train[TARGET])
    y_test = np.log10(test[TARGET])
    return train[FEATURES], test[FEATURES], y_train, y_test


if __name__ == "__main__":
    data = load_model_data()
    X_train, X_test, y_train, y_test = time_split(data)
    print("rows used (positive amounts):", len(data))
    print("train:", X_train.shape, "years", X_train["fiscal_year"].min(), "-", X_train["fiscal_year"].max())
    print("test: ", X_test.shape, "years", X_test["fiscal_year"].min(), "-", X_test["fiscal_year"].max())
    print("target log10 train: mean", round(y_train.mean(), 2), "std", round(y_train.std(), 2))
    print("target log10 test:  mean", round(y_test.mean(), 2), "std", round(y_test.std(), 2))