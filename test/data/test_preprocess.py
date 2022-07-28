import numpy as np
import pandas as pd

from src.data.preprocess import remove_irrelevant_columns, fill_na_for_numeric_columns_with_mean, \
    fill_na_for_categorical_columns, fill_na_for_categorical_columns_with_condition


class TestPreprocessing:
    def test_remove_irrelevant_columns(self):
        # given
        dataframe = pd.DataFrame({'relevant_col1': [1, 2], 'relevant_col2': [3, 4], 'irrelevant_col3': [5, 6]})

        # when
        dataframe_with_relevant_columns = remove_irrelevant_columns(dataframe, ['irrelevant_col3'])

        # then
        pd.testing.assert_frame_equal(dataframe_with_relevant_columns,
                                      pd.DataFrame({'relevant_col1': [1, 2], 'relevant_col2': [3, 4]}))

    def test_fill_na_numeric_columns_with_mean(self):
        # given
        dataframe = pd.DataFrame({'col1': [4, 2, np.nan], 'col2': [6, np.nan, 4]}, dtype=np.float64)

        # when
        new_dataframe = fill_na_for_numeric_columns_with_mean(dataframe, 'col1')

        # then
        pd.testing.assert_frame_equal(new_dataframe,
                                      pd.DataFrame({'col1': [4, 2, 3], 'col2': [6, np.nan, 4]}, dtype=np.float64))

    def test_fill_na_for_categorical_columns(self):
        # given
        dataframe = pd.DataFrame({'col1': ['A', 'B', np.nan, 'B'], 'col2': [6, 5, 4, 6]})

        # when
        new_dataframe = fill_na_for_categorical_columns(dataframe, 'col1')

        # then
        pd.testing.assert_frame_equal(new_dataframe,
                                      pd.DataFrame({'col1': ['A', 'B', 'B', 'B'], 'col2': [6, 5, 4, 6]}))

    def test_fill_na_for_categorical_columns_with_condition(self):
        # given
        dataframe = pd.DataFrame({'col1': ['A', 'B', np.nan, np.nan], 'col2': [6, 5, 4, 6]})
        condition = dataframe.col2 == 6

        # when
        new_dataframe = fill_na_for_categorical_columns_with_condition(dataframe, 'col1', condition)

        # then
        pd.testing.assert_frame_equal(new_dataframe,
                                      pd.DataFrame({'col1': ['A', 'B', np.nan, 'A'], 'col2': [6, 5, 4, 6]}))
