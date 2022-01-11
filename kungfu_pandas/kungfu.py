from typing import Any, Callable, Dict, List, Tuple, Union

import numpy as np
import pandas as pd


def mask(df: pd.DataFrame, key: str, function: Callable) -> pd.DataFrame:
    """
    Returns a filtered dataframe, by applying function to key

    Arguments:
        df: dataframe to be masked.
        key: column name of the dataframe to apply function to.
        function: function applied to the key for filtering.

    Usage:

    ```python
    import pandas as pd
    from kungfu_pandas import mask

    df = pd.DataFrame({
            'x': [1, 2, 3, 0, 0, 1],
            'group': ['a', 'a', 'a', 'b', 'b', 'b']
    })

    def is_zero(x):
        return x == 0

    (
        df
        .pipe(mask, 'x', is_zero)
    )

    ```
    """
    return df[function(df[key])]


def count(df: pd.DataFrame, by: str = None) -> pd.DataFrame:
    """
    Counts by column, if no column is given just gives total count

    Arguments:
        df: dataframe to count.
        by: column name of the dataframe to group and count by.

    Usage:

    ```python
    import pandas as pd
    from kungfu_pandas import count

    df = pd.DataFrame({
            'x': [1, 2, 3, 0, 0, 1],
            'group': ['a', 'a', 'a', 'b', 'b', 'b']
    })

    (
        df
        .pipe(count, by='group')
    )
    ```
    """
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
    Groups by column 'by', aggregates column 'col' with 'agg'
    and orders by their values ascending or descedning

    Arguments:
        df: dataframe to count.
        by: column name of the dataframe to group by.
        col: column name of the dataframe to summarise.
        agg: aggregation function to summarise col.
        asc: sort by aggregation result, ascending or descending.

    Usage:

    ```python
    import pandas as pd
    from kungfu_pandas import count

    df = pd.DataFrame({
            'x': [1, 2, 3, 0, 0, 1],
            'group': ['a', 'a', 'a', 'b', 'b', 'b']
    })

    (
        df
        .pipe(agg_by_col, by='group', col='x', agg='mean')
    )
    ```
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


def case_when(
    df: pd.DataFrame,
    cases: Union[Dict[Callable, Any], List[Tuple[Callable, Any]]],
) -> pd.Series:
    """
    This is the pandas equivalent of SQL case when. If no cases match, NaN is returned.

    Arguments:
        df: dataframe to apply case when to.
        cases: dictionary of functions and their output values. It can also be a list of tuples where the first element should be the function and the second the value. It is important to note that this dictionary is ordered as in a sql case when

    Usage:

    ```python
    import pandas as pd
    from kungfu_pandas import case_when

    df = pd.DataFrame({
            'x': [1, 2, 3, 0, 0, 1],
            'group': ['a', 'a', 'a', 'b', 'b', 'b']
    })

    (
        df
        .pipe(case_when, [
            (lambda d: d['x'] == 0, 0),
            (lambda d: (d['x'] == 1) & (d['group'] == 'a'), 1),
            (lambda d: (d['x'] == 1) & (d['group'] == 'b'), 2),
            (lambda d: d['x'] >= 3, 3),
        ])
    )

    (
        df
        .assign(
            new_x=lambda old_df:
            case_when(old_df, {
                lambda d: d['x'] == 0: 0,
                lambda d: (d['x'] == 1) & (d['group'] == 'a'): 1,
                lambda d: (d['x'] == 1) & (d['group'] == 'b'): 2,
                lambda d: d['x'] >= 3: 3,
            })
        )
    )
    ```
    """
    if not cases:
        raise ValueError(
            'Empty condition: value dictionary is passed to case_when')

    cases = cases.copy()
    # Transform to list of tuples
    if isinstance(cases, dict):
        cases = list(cases.items())
    # Output type
    type_out = type(cases[0][1])

    # Initialize out_s as a series full of None
    out_s = pd.Series(np.nan, index=df.index, dtype=type_out)

    # We need to reverse the order of the dictionary to have the same logic as case when in sql
    # The idea is that the first condition rules out the rest of the conditions,
    # the second rules out the latter ones, etc.
    for lmbd, value in reversed(cases):
        out_s[lmbd(df)] = value
    return out_s
