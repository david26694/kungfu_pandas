# Kungfu pandas

Set of functions that help you work with pandas dataframes. Docs are in [here](https://david26694.github.io/kungfu_pandas/index.html).

## Basic example


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
This is what we get back:

```python
  group  n
0     a  3
1     b  3
```


## Features

Functions in this library are:

* `count`: To easily count number of rows per group.
* `mask`: To filter by applying a function on a row.
* `agg_by_col`: To perform aggregations on a column grouping by another column.
* `case_when`: Create a new series based on a series of case when statements.


## Installation

You can install this package via `pip`.

```
pip install kungfu_pandas
```

## Contributing

To get started locally, you can clone
the repo and quickly get started using the `Makefile`.

```
git clone git@github.com:david26694/kungfu_pandas.git
cd kungfu_pandas
make install-dev
```
