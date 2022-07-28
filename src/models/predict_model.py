import pickle
import numpy as np
import pandas as pd


def make_predictions(data_for_prediction: pd.DataFrame, model_path: str) -> np.array:
    model = pickle.load(open(model_path, 'wb'))
    return model.predict(data_for_prediction)
