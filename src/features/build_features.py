import math
import pickle

import pandas as pd
from pickle import dump
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

IRRELEVANT_COLUMNS = ['score', 'p1_df', 'p2_df', 'p1_bpFaced', 'p2_bpFaced', 'p1_bpSaved', 'p2_bpSaved',
                      'p1_svpt', 'p2_svpt', 'p1_1stIn', 'p2_1stIn', 'p1_1stWon', 'p2_1stWon', 'p1_SvGms',
                      'p2_SvGms', 'p1_2ndWon', 'p2_2ndWon', 'p1_ace', 'p2_ace', 'best_of', 'minutes']

COLUMNS_WITH_TOO_MANY_CATEGORIES = ['p2_name', 'tourney_id', 'p1_name']


def extract_month_from_date(df: pd.DataFrame, column_to_use: str, column_to_create: str) -> pd.DataFrame:
    """
    Extracting the month from a date with the followinf format : yyyymmdd
    """
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
    data = remove_irrelevant_columns(raw_data, IRRELEVANT_COLUMNS)
    data = convert_object_to_category(data)
    data[["p1_rank", "p2_rank"]] = data[["p1_rank", "p2_rank"]].astype('category')
    data = data.drop(columns=['p1_entry', 'p2_entry'])

    list_of_numeric_columns_with_missing_values = ['p1_age', 'p2_age', 'p1_ht', 'p2_ht']
    for element in list_of_numeric_columns_with_missing_values:
        data = fill_na_for_numeric_columns_with_mean(data, element)

    list_of_categorical_columns_with_missing_values = ['p1_hand', 'p2_hand']
    for element in list_of_categorical_columns_with_missing_values:
        data = fill_na_for_categorical_columns(data, element)

    data.loc[data.p1_hand == 'U', 'p1_hand'] = 'R'
    data.loc[data.p2_hand == 'U', 'p2_hand'] = 'R'
    data['p1_hand'] = data['p1_hand'].astype('category')
    data['p2_hand'] = data['p2_hand'].astype('category')

    data = data.drop(columns=COLUMNS_WITH_TOO_MANY_CATEGORIES)
    data[["p1_id", "p2_id"]] = data[["p1_id", "p2_id"]].astype('category')

    data = extract_month_from_date(data, 'tourney_date', 'tourney_month')

    data = define_seed_player(data, 'p1_seed', 'p1_is_seed_player')
    data = define_seed_player(data, 'p2_seed', 'p2_is_seed_player')

    data = define_ranking_category(data, 'p1_rank', 'p1_new_rank')
    data = define_ranking_category(data, 'p2_rank', 'p2_new_rank')

    columns_to_drop = ['p1_seed', 'p2_seed', 'tourney_date', 'p1_rank', 'p2_rank']
    data = data.drop(columns=columns_to_drop)

    list_of_new_categorical_columns_with_missing_values = ['p1_new_rank', 'p2_new_rank']
    for element in list_of_new_categorical_columns_with_missing_values:
        data = fill_na_for_categorical_columns(data, element)

    list_of_rank_points_columns = ['p1_rank_points', 'p2_rank_points']
    for element in list_of_rank_points_columns:
        data = fill_na_for_categorical_columns_with_condition(data, element, data.p1_new_rank == 'Top 30')
        data = fill_na_for_categorical_columns_with_condition(data, element, data.p1_new_rank == 'Top 30-100')
        data = fill_na_for_categorical_columns_with_condition(data, element, data.p1_new_rank == 'Under 100')

    features = data.drop(columns=['p1_won'])
    if train_or_test == 'train':
        numeric_columns = features.select_dtypes(['int64', 'float64']).columns
        scaler = StandardScaler()
        scaler.fit(data[numeric_columns])
    else:
        with open('../../models/scaler.pkl', 'rb') as f:
            scaler = pickle.load(f)
    data[numeric_columns] = scaler.transform(data[numeric_columns])
    return data
