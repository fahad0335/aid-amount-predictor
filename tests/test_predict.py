# Name: Shah Fahad  Roll no: TRN-2026-000706  Date: 19-11-2026
import pandas as pd
import pytest
from src.predict import validate_columns
from src.model_data import FEATURES


def test_validate_columns_passes_with_all_features():
    validate_columns(pd.DataFrame(columns=FEATURES))


def test_validate_columns_fails_when_column_missing():
    df = pd.DataFrame(columns=FEATURES[:-1])
    with pytest.raises(ValueError):
        validate_columns(df)
