from kungfu_pandas import count
import pandas as pd


def test_count_single(groups_df):
    """Count without groups"""

    pd.testing.assert_frame_equal(
        count(groups_df),
        pd.DataFrame({'n': [6]})
    )


def test_count_group(groups_df):
    """Count with groups"""

    pd.testing.assert_frame_equal(
        count(groups_df, by='group'),
        pd.DataFrame({'group': ['a', 'b'], 'n': [3, 3]})
    )


def test_empty_counts(empty_df):
    """Count with and without groups, but empty input"""

    pd.testing.assert_frame_equal(
        count(empty_df),
        pd.DataFrame({'n': [0]})
    )

    pd.testing.assert_frame_equal(
        count(empty_df, by='y'),
        pd.DataFrame({'y': [None], 'n': [0]})
    )
