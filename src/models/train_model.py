import logging
import pandas as pd
from catboost import CatBoostClassifier
from src.utils.utils import extract_categorical_indexes_from_df, preprocess


def train_model(dataframe: pd.DataFrame, target_column: str) -> CatBoostClassifier:
    df = preprocess(dataframe)
    X = df.drop(columns=[target_column])
    y = df[target_column]
    categorical_indexes = extract_categorical_indexes_from_df(X)
    model = CatBoostClassifier(
        random_seed=0,
        cat_features=categorical_indexes,
        eval_metric="Precision",
        iterations=1500,
        learning_rate=0.05,
        max_depth=4,
    )
    model.fit(X, y)
    model.save_model('../../models/catboost_model.pkl')
    return model


if __name__ == '__main__':
    data = pd.read_csv("../../data/processed/data_preprocessed.csv")
    logging.info("Training ...")
    preprocessed_data = train_model(dataframe=data, target_column='p1_won')
    logging.info("Training done")
