import pytest
import pandas as pd


@pytest.fixture(scope="module")
def simple_df():
    return pd.DataFrame({
        'x': [1, 2, 3]
    })


@pytest.fixture(scope="module")
def empty_df():
    return pd.DataFrame(columns=['x', 'y'])


@pytest.fixture(scope="module")
def groups_df():
    return pd.DataFrame({
        'x': [1, 2, 3, 0, 0, 1],
        'group': ['a', 'a', 'a', 'b', 'b', 'b']
    })
