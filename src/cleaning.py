# Name: Shah Fahad  Roll no: TRN-2026-000706  Date: 19-11-2026
# Purpose: raw data ko clean karne wale functions.
import pandas as pd


def remove_duplicates(df):
    """Remove rows that are exact copies of another row.
    Returns a new DataFrame. The input DataFrame is not changed.
    """
    return df.drop_duplicates().reset_index(drop=True)

def parse_dates(df, columns):
    """Convert text date columns to real datetime values.

    Values that are missing or cannot be read become NaT (missing date).
    Returns a new DataFrame. The input DataFrame is not changed.
    """
    result = df.copy()
    for col in columns:
        result[col] = pd.to_datetime(result[col], errors="coerce", utc=True)
    return result

def fill_missing_categories(df, columns, fill_value="Unknown"):
    """Fill missing text values in the given columns with fill_value.

    Returns a new DataFrame. The input DataFrame is not changed.
    """
    result = df.copy()
    for col in columns:
        result[col] = result[col].fillna(fill_value)
    return result


def flag_negative_amounts(df, column="current_amount"):
    """Add a True/False column marking rows where the amount is negative.

    Rows are kept (not deleted). Returns a new DataFrame.
    """
    result = df.copy()
    result["is_negative_amount"] = result[column] < 0
    return result