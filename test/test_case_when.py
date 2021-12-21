from kungfu_pandas import case_when
import pandas as pd


def test_case_when_simple(groups_df):
    """Case when simple"""

    out = (
        groups_df
        .pipe(case_when, {
            lambda d: d['x'] == 0: 0,
            lambda d: (d['x'] == 1) & (d['group'] == 'a'): 1,
            lambda d: (d['x'] == 1) & (d['group'] == 'b'): 2,
            lambda d: d['x'] >= 3: 3,
        })
    )

    pd.testing.assert_series_equal(
        out,
        pd.Series([1, None, 3, 0, 0 , 2])
    )


def test_case_when_order(groups_df):
    """Case when order matters"""

    out = (
        groups_df
        .pipe(case_when, {
            lambda d: d['x'] >= 0: 0,
            lambda d: d['x'] >= 1: 1,
        })
    )

    pd.testing.assert_series_equal(
        out,
        pd.Series([0.0] * 6)
    )


def test_case_when_empty(empty_df):
    """Case when empty"""

    pd.testing.assert_series_equal(
        case_when(empty_df, {lambda d: d['x'] == 0: 0.0}),
        pd.Series(dtype='float64')
    )
