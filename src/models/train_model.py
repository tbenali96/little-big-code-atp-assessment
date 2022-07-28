import pandas as pd
from catboost import CatBoostClassifier
from src.utils.utils import extract_categorical_indexes_from_df


def train_model(data: pd.DataFrame, target_column: str) -> CatBoostClassifier:
    X = data.drop(columns=[target_column])
    y = data[target_column]
    categorical_indexes = extract_categorical_indexes_from_df(data)
    model = CatBoostClassifier(iterations=1500,
                               learning_rate=0.01,
                               depth=2)
    model.fit(X, y, categorical_indexes)
    model.save_model('../models/catboost_model.pkl')
    return model
