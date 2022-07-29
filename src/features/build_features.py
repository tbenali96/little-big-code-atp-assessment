import math
import pandas as pd
from pickle import dump
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler


def extract_month_from_date(df: pd.DataFrame, column_to_use: str, column_to_create: str) -> pd.DataFrame:
    df[column_to_create] = df[column_to_use].apply(lambda x: int(str(x)[4:6]))
    return df


def define_seed_player(df: pd.DataFrame, column_to_use: str, column_to_create: str) -> pd.DataFrame:
    df[column_to_create] = df[column_to_use].apply(lambda x: int(not math.isnan(x)))
    return df


def define_ranking_category(df: pd.DataFrame, column_to_use: str, column_to_create: str) -> pd.DataFrame:
    def define_rank(x):
        if x < 31:
            return 'Top 30'
        elif x < 101:
            return 'Top 30-100'
        else:
            return 'Under 100'

    df[column_to_create] = df[column_to_use].apply(lambda x: define_rank(x))
    return df


def remove_irrelevant_columns(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    return df.drop(columns=columns)


def fill_na_for_numeric_columns_with_mean(df: pd.DataFrame, column: str) -> pd.DataFrame:
    df[column] = df[column].fillna(df[column].mean())
    return df


def fill_na_for_categorical_columns(df: pd.DataFrame, column: str) -> pd.DataFrame:
    col_imputer = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
    col_imputer.fit(df[[column]])
    df[column] = col_imputer.transform(df[[column]])
    return df


def fill_na_for_categorical_columns_with_condition(df: pd.DataFrame, column: str, condition: bool) -> pd.DataFrame:
    col_imputer = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
    col_imputer.fit(df[condition][[column]])
    df.loc[condition, column] = col_imputer.transform(df[condition][[column]])
    return df


def scale_features(df: pd.DataFrame, columns_to_scale: list) -> pd.DataFrame:
    scaler = StandardScaler()
    scaler.fit(df[columns_to_scale])
    df[columns_to_scale] = scaler.transform(df[columns_to_scale])
    dump(scaler, open('../models/scaler.pkl', 'wb'))
    return df


def convert_object_to_category(df: pd.DataFrame) -> pd.DataFrame:
    object_columns = df.select_dtypes(['object']).columns
    df[object_columns] = df[object_columns].astype('category')
    return df


def build_features(raw_data: pd.DataFrame, train_or_test: str) -> pd.DataFrame:
    convert_object_to_category(raw_data)
    pass


