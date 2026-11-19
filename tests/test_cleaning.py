# Name: Shah Fahad  Roll no: TRN-2026-000706  Date: 19-11-2026
import pandas as pd
from src.cleaning import remove_duplicates


def test_remove_duplicates_removes_exact_copies():
    df = pd.DataFrame({"a": [1, 1, 2], "b": ["x", "x", "y"]})
    result = remove_duplicates(df)
    assert len(result) == 2


def test_remove_duplicates_does_not_change_input():
    df = pd.DataFrame({"a": [1, 1, 2], "b": ["x", "x", "y"]})
    remove_duplicates(df)
    assert len(df) == 3