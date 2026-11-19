# Name: ...  Roll no: ...  Date: ...
# Purpose: raw data ko clean karne wale functions.
import pandas as pd


def remove_duplicates(df):
    """Remove rows that are exact copies of another row.
    Returns a new DataFrame. The input DataFrame is not changed.
    """
    return df.drop_duplicates().reset_index(drop=True)