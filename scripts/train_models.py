
import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import KFold, cross_validate
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = BASE_DIR / "data" / "crop_yield.csv"
RESULT_PATH = BASE_DIR / "results" / "model_comparison.csv"

df = pd.read_csv(DATA_PATH)
X = df[["Fert", "Water"]]
y = df["Yield"]

preprocessor = ColumnTransformer(
    transformers=[
        ("cat", Pipeline(steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore"))
        ]), ["Fert", "Water"])
    ],
    remainder="drop"
)

models = {
    "LinearRegression": LinearRegression(),
    "DecisionTree": DecisionTreeRegressor(random_state=42, max_depth=3),
    "RandomForest": RandomForestRegressor(random_state=42, n_estimators=200, max_depth=4),
    "GradientBoosting": GradientBoostingRegressor(random_state=42, n_estimators=100, learning_rate=0.05, max_depth=2),
    "SVR": SVR(kernel="rbf", C=10, epsilon=0.1),
}

cv = KFold(n_splits=5, shuffle=True, random_state=42)

results = []
for name, model in models.items():
    pipe = Pipeline(steps=[
        ("preprocessor", preprocessor),
        ("model", model)
    ])

    scores = cross_validate(
        pipe,
        X,
        y,
        cv=cv,
        scoring={
            "rmse": "neg_root_mean_squared_error",
            "mae": "neg_mean_absolute_error",
            "r2": "r2"
        }
    )

    results.append({
        "Model": name,
        "RMSE_mean": -scores["test_rmse"].mean(),
        "MAE_mean": -scores["test_mae"].mean(),
        "R2_mean": scores["test_r2"].mean()
    })

results_df = pd.DataFrame(results).sort_values("RMSE_mean")
results_df.to_csv(RESULT_PATH, index=False)

print("\nComparação de modelos:")
print(results_df.to_string(index=False))
print("\nMelhor modelo:", results_df.iloc[0]["Model"])
