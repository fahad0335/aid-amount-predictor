# Name: Shah Fahad  Roll no: TRN-2026-000706  Date: 19-11-2026
import pandas as pd
from src.cleaning import parse_dates, remove_duplicates


def test_remove_duplicates_removes_exact_copies():
    df = pd.DataFrame({"a": [1, 1, 2], "b": ["x", "x", "y"]})
    result = remove_duplicates(df)
    assert len(result) == 2


def test_remove_duplicates_does_not_change_input():
    df = pd.DataFrame({"a": [1, 1, 2], "b": ["x", "x", "y"]})
    remove_duplicates(df)
    assert len(df) == 3
    
def test_parse_dates_makes_datetime_and_keeps_missing():
    df = pd.DataFrame({"d": ["2001-11-16 00:00:00 UTC", None]})
    result = parse_dates(df, ["d"])
    assert pd.api.types.is_datetime64_any_dtype(result["d"])
    assert result["d"].isna().sum() == 1


def test_parse_dates_turns_bad_text_into_missing():
    df = pd.DataFrame({"d": ["not a date"]})
    result = parse_dates(df, ["d"])
    assert result["d"].isna().sum() == 1
    