# Name: Shah Fahad  Roll no: TRN-2026-000706  Date: 19-11-2026
import pandas as pd
import pytest
from src.cleaning import remove_duplicates, parse_dates, fill_missing_categories, flag_negative_amounts
from src.validation import check_no_missing, check_range
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
    
def test_fill_missing_categories():
    df = pd.DataFrame({"a": ["x", None]})
    result = fill_missing_categories(df, ["a"])
    assert result["a"].tolist() == ["x", "Unknown"]
    assert df["a"].isna().sum() == 1


def test_flag_negative_amounts():
    df = pd.DataFrame({"current_amount": [5, -3]})
    result = flag_negative_amounts(df)
    assert result["is_negative_amount"].tolist() == [False, True]
    assert len(df.columns) == 1


def test_check_no_missing_passes_and_fails():
    check_no_missing(pd.DataFrame({"a": [1]}), ["a"])
    with pytest.raises(ValueError):
        check_no_missing(pd.DataFrame({"a": [None]}), ["a"])


def test_check_range_passes_and_fails():
    check_range(pd.DataFrame({"y": [2001, 2021]}), "y", 2001, 2021)
    with pytest.raises(ValueError):
        check_range(pd.DataFrame({"y": [1999]}), "y", 2001, 2021)
    
