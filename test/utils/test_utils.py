import pandas as pd
from src.utils.utils import extract_categorical_indexes_from_df


def test_extract_categorical_indexes_from_df():
    # given
    dataframe = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6], 'col3': ['A', 'B', 'C'], 'col4': [4, 5, 6],
                              'col5': ['A', 'B', 'C']})
    dataframe = dataframe.astype({'col1': int, 'col2': int, 'col3': 'category', 'col4': int,
                                  'col5': 'category'})

    # when
    categorical_indexes = extract_categorical_indexes_from_df(dataframe)

    # then
    assert categorical_indexes == [2, 4]

