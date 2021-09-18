from kungfu_pandas import mask
import pandas as pd


def test_mask(simple_df):
    """Test whether mask filters wanted elements"""

    def higher_2(x):
        return x > 2

    masked_df = mask(simple_df, 'x', higher_2)
    masked_df = masked_df.reset_index(drop=True)
    pd.testing.assert_frame_equal(
        masked_df,
        pd.DataFrame(dict(x=[3]))
    )


def test_mask_empty(empty_df):
    """If input is empty, output should be empty"""
    def higher_2(x):
        return x > 2
    pd.testing.assert_frame_equal(
        mask(empty_df, 'x', higher_2),
        empty_df
    )


def test_mask_return_empty(simple_df):
    """When there's no match, we should have 0 rwos"""

    def higher_3(x):
        return x > 3

    masked_df = mask(simple_df, 'x', higher_3)
    masked_df = masked_df.reset_index(drop=True)

    assert masked_df.shape[0] == 0
