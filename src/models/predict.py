import logging

import numpy as np
import pandas as pd
from catboost import CatBoostClassifier

from src.features.build_features import build_features
from src.utils.utils import preprocess


def make_predictions(data_for_prediction: pd.DataFrame, model_path: str) -> np.array:
    logging.info("Building the features for the test dataset")
    data = build_features(raw_data=data_for_prediction, train_or_test="test")
    logging.info("Feature Engineering done")
    data = preprocess(data)
    model = CatBoostClassifier()
    model.load_model(model_path)
    return model.predict(data)


if __name__ == '__main__':
    test_data = pd.read_csv("../../data/test/sample.csv")
    logging.info("Predicting ...")
    predictions = make_predictions(
        data_for_prediction=test_data, model_path="../../models/catboost_model.pkl"
    )
    logging.info("Prediction done")
    print(f'The results of your predictions are : {predictions}')
