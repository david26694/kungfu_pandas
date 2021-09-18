import pandas as pd
from typing import Callable


def mask(df: pd.DataFrame, key: str, function: Callable) -> pd.DataFrame:
    """Returns a filtered dataframe, by applying function to key"""
    return df[function(df[key])]


def count(df: pd.DataFrame, by: str) -> pd.DataFrame:
    """Counts by column, if no column is given just gives total count"""
    if by:
        return (
            df
            .groupby(by)
            .size()
            .to_frame()
            .reset_index()
            .rename(columns={0: 'n'})
        )
    else:
        return pd.DataFrame(dict(n=df.shape[0]))


def agg_by_col(
    df: pd.DataFrame,
    by: str,
    col: str,
    agg: str = 'sum',
    asc: bool = False
):
    """
    Groups by column 'by',
    aggregates column 'col' with 'agg'
    and orders by their values ascending or descedning
    """
    return (
        df
        .groupby(by, as_index=False)
        [col]
        .agg(agg)
        .sort_values(by=col, ascending=asc)
    )
