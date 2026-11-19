# Name: Shah Fahad  Roll no: TRN-2026-000706  Date: 19-11-2026
# Purpose: check if the data is valid.if not, raise ValueError with a message.


def check_no_missing(df, columns):
    """Raise ValueError if any of the given columns has missing values."""
    for col in columns:
        n = df[col].isna().sum()
        if n > 0:
            raise ValueError(f"Column '{col}' has {n} missing values")


def check_range(df, column, low, high):
    """Raise ValueError if any value in the column is outside low..high."""
    bad = df[(df[column] < low) | (df[column] > high)]
    if len(bad) > 0:
        raise ValueError(f"Column '{column}' has {len(bad)} values outside {low}-{high}")