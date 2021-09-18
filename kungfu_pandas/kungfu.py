import pandas as pd

def _mask(df, key, function):
  """Returns a filtered dataframe, by applying function to key"""
  return df[function(df[key])]