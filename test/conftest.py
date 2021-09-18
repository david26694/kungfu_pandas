import pytest

from kungfu_pandas import mask
import pandas as pd


@pytest.fixture(scope="module")
def simple_df():
    return pd.DataFrame({
        'x': [1, 2, 3]
    })
