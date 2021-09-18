import pandas as pd
from typing import Callable


def mask(df: pd.DataFrame, key: str, function: Callable) -> pd.DataFrame:
    """Returns a filtered dataframe, by applying function to key"""
    return df[function(df[key])]


def count(df: pd.DataFrame, by: str = None) -> pd.DataFrame:
    """Counts by column, if no column is given just gives total count"""
    if not by:
        # Not grouping, just return the shape
        return pd.DataFrame(dict(n=[df.shape[0]]))

    if df.shape[0] == 0:
        # Edge case -> 0 rows but using groups
        return pd.DataFrame({by: [None], 'n': [0]})
    # Regular case
    return (
        df
        .groupby(by)
        .size()
        .to_frame()
        .reset_index()
        .rename(columns={0: 'n'})
    )


def agg_by_col(
    df: pd.DataFrame,
    by: str = None,
    col: str = None,
    agg: str = 'sum',
    asc: bool = False
) -> pd.DataFrame:
    """
    Groups by column 'by',
    aggregates column 'col' with 'agg'
    and orders by their values ascending or descedning
    """

    # Edge case -> 0 rows
    if df.shape[0] == 0:
        if by:
            return pd.DataFrame({by: [None], col: [None]})
        else:
            return pd.DataFrame({col: [None]})

    if by:
        return (
            df
            .groupby(by, as_index=False)
            [col]
            .agg(agg)
            .sort_values(by=col, ascending=asc)
        )
    else:
        return pd.DataFrame(
            {col: [df[col].agg(agg)]}
        ).sort_values(by=col, ascending=asc)
