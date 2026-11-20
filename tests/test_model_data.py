# Name: Shah Fahad  Roll no: TRN-2026-000706  Date: 19-11-2026
import pandas as pd
from src.model_data import time_split, FEATURES, TARGET


def make_df():
    data = {col: ["a"] * 4 for col in FEATURES}
    data["fiscal_year"] = [2010, 2017, 2018, 2020]
    data[TARGET] = [100, 1000, 10, 100000]
    return pd.DataFrame(data)


def test_time_split_has_no_overlap_in_years():
    X_train, X_test, y_train, y_test = time_split(make_df())
    assert X_train["fiscal_year"].max() <= 2017
    assert X_test["fiscal_year"].min() > 2017


def test_target_is_not_in_features():
    X_train, X_test, _, _ = time_split(make_df())
    assert TARGET not in X_train.columns


def test_target_is_log10():
    _, _, y_train, _ = time_split(make_df())
    assert y_train.tolist() == [2.0, 3.0]
