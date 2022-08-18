import pandas as pd


def extract_categorical_indexes_from_df(df: pd.DataFrame) -> list:
    categorical_columns = df.select_dtypes(['category']).columns
    categorical_indexes = []
    for element in categorical_columns:
        categorical_indexes.append(df.columns.to_list().index(element))
    return categorical_indexes


def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    df[["p1_id", "p2_id"]] = df[["p1_id", "p2_id"]].astype('category')
    object_columns = df.select_dtypes(['object']).columns
    df[object_columns] = df[object_columns].astype('category')
    return df