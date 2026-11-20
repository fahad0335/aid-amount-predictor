# Name: Shah Fahad  Roll no: TRN-2026-000706  Date: 19-11-2026
import pandas as pd
from sklearn.dummy import DummyRegressor
from src.model_data import FEATURES
from src.pipeline import build_pipeline


def make_X(categories):
    data = {col: categories for col in FEATURES}
    data["fiscal_year"] = [2010] * len(categories)
    return pd.DataFrame(data)


def test_pipeline_handles_unseen_category():
    pipe = build_pipeline(DummyRegressor())
    pipe.fit(make_X(["a", "b"]), [1.0, 2.0])
    result = pipe.predict(make_X(["never_seen"]))
    assert len(result) == 1


def test_pipeline_handles_missing_values():
    pipe = build_pipeline(DummyRegressor())
    X = make_X(["a", None])
    pipe.fit(X, [1.0, 2.0])
    assert len(pipe.predict(X)) == 2
