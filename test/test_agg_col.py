from kungfu_pandas import agg_by_col
import pandas as pd


def test_agg_simple(groups_df):
    """Agg without groups"""

    pd.testing.assert_frame_equal(
        agg_by_col(groups_df, col='x'),
        pd.DataFrame({'x': [7]})
    )


def test_agg_group(groups_df):
    """Agg with groups"""
    agg_df = agg_by_col(groups_df, by='group', col='x')
    pd.testing.assert_frame_equal(
        agg_df,
        pd.DataFrame({'group': ['a', 'b'], 'x': [6, 1]})
    )


def test_agg_empty(empty_df):
    """Count with and without groups, but empty input"""

    pd.testing.assert_frame_equal(
        agg_by_col(empty_df, col='x'),
        pd.DataFrame({'x': [None]})
    )

    pd.testing.assert_frame_equal(
        agg_by_col(empty_df, by='y', col='x'),
        pd.DataFrame({'y': [None], 'x': [None]})
    )
