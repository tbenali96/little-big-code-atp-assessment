import numpy as np
import pandas as pd
from src.features.build_features import extract_month_from_date, define_seed_player, define_ranking_category


class TestFeatures:
    def test_extract_month_from_date(self):
        # given
        dataframe = pd.DataFrame({'col1': [1, 2, 3], 'col_date': [20150816, 20180728, 20160606]})

        # when
        dataframe_with_month_column = extract_month_from_date(dataframe, 'col_date', 'col_month')

        # then
        pd.testing.assert_frame_equal(dataframe_with_month_column,
                                      pd.DataFrame({'col1': [1, 2, 3], 'col_date': [20150816, 20180728, 20160606],
                                                    'col_month': [8, 7, 6]}))

    def test_define_seed_player(self):
        # given
        dataframe = pd.DataFrame({'id_player': [1, 2, 3], 'player_seed': [1, 4, np.nan]})

        # when
        new_dataframe = define_seed_player(dataframe, 'player_seed', 'is_seed_player')

        # then
        pd.testing.assert_frame_equal(new_dataframe,
                                      pd.DataFrame({'id_player': [1, 2, 3], 'player_seed': [1, 4, np.nan],
                                                    'is_seed_player': [1, 1, 0]}))

    def test_define_ranking_category(self):
        # given
        dataframe = pd.DataFrame({'id_player': [1, 2, 3, 5, 6, 10], 'player_rank': [1, 20, 45, 10, 150, 67]})

        # when
        new_dataframe = define_ranking_category(dataframe, 'player_rank', 'player_rank_category')

        # then
        pd.testing.assert_frame_equal(new_dataframe,
                                      pd.DataFrame({'id_player': [1, 2, 3, 5, 6, 10],
                                                    'player_rank': [1, 20, 45, 10, 150, 67],
                                                    'player_rank_category': ['Top 30', 'Top 30', 'Top 30-100', 'Top 30',
                                                                             'Under 100', 'Top 30-100']}))
