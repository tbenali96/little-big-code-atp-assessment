import math
import pandas as pd


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
