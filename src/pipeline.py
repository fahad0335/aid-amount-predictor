# Name: Shah Fahad  Roll no: TRN-2026-000706  Date: 20-11-2026
# Purpose: preprocessing + scikit-learn pipeline.
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.model_data import CATEGORICAL_FEATURES, NUMERIC_FEATURES


def build_preprocessor():
    """Imputation + encoding + scaling. Nothing is fitted here."""
    categorical = Pipeline([
        ("impute", SimpleImputer(strategy="constant", fill_value="Unknown")),
        ("encode", OneHotEncoder(handle_unknown="ignore")),
    ])
    numeric = Pipeline([
        ("impute", SimpleImputer(strategy="median")),
        ("scale", StandardScaler()),
    ])
    return ColumnTransformer([
        ("cat", categorical, CATEGORICAL_FEATURES),
        ("num", numeric, NUMERIC_FEATURES),
    ])


def build_pipeline(model):
    """One object: preprocessing first, then the given model."""
    return Pipeline([
        ("preprocess", build_preprocessor()),
        ("model", model),
    ])


if __name__ == "__main__":
    from sklearn.dummy import DummyRegressor
    from sklearn.metrics import mean_absolute_error
    from src.model_data import load_model_data, time_split

    X_train, X_test, y_train, y_test = time_split(load_model_data())
    pipe = build_pipeline(DummyRegressor(strategy="median"))
    pipe.fit(X_train, y_train)  # fit sirf train par
    print("Features after encoding:", pipe.named_steps["preprocess"].transform(X_train).shape[1])
    print("Baseline MAE on test (log10 scale):", round(mean_absolute_error(y_test, pipe.predict(X_test)), 3))