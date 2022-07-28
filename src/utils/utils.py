import pandas as pd


def extract_categorical_indexes_from_df(df: pd.DataFrame):
    categorical_columns = df.select_dtypes(['category']).columns
    categorical_indexes = []
    for element in categorical_columns:
        categorical_indexes.append(df.columns.to_list().index(element))
    return categorical_indexes
