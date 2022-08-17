import pandas as pd
from src.app.app import extract_date


class TestApp():
    def test_extract_date(self):
        # given
        dataframe = pd.DataFrame({'col1': [1, 2, 3], 'tourney_date': [20150816, 20180728, 20160606]})

        # when
        dataframe_with_date = extract_date(dataframe)

        # then
        pd.testing.assert_frame_equal(dataframe_with_date,
                                      pd.DataFrame({'col1': [1, 2, 3],
                                                    'tourney_date': [20150816, 20180728, 20160606],
                                                    'date': [pd.to_datetime(str(20150816), format='%Y%m%d'),
                                                             pd.to_datetime(str(20180728), format='%Y%m%d'),
                                                             pd.to_datetime(str(20160606), format='%Y%m%d')],
                                                    'year': [2015, 2018, 2016]}),
                                      check_dtype=False,
                                      check_datetimelike_compat=False)
