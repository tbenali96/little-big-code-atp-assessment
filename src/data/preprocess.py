from pickle import dump
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler


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


def scale_features(df, columns_to_scale):
    scaler = StandardScaler()
    scaler.fit(df[columns_to_scale])
    df[columns_to_scale] = scaler.transform(df[columns_to_scale])
    dump(scaler, open('../models/scaler.pkl', 'wb'))
    return df


