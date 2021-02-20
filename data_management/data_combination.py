"""Author - Sam Hollings
This file contains functions for joining to together dataframes of patient data in a consistent way
"""
import pandas as pd
import numpy as np


def join_longways(list_of_dataframes):
    """Join the supplied dataframes along the long axis - appending them one after another to make a longer table"""
    df = pd.concat(list_of_dataframes,axis=0)

    return df


def join_widthways(df1 : pd.DataFrame, df2: pd.DataFrame, key, where_clause=None, how='left' ):
    """Join the supplied dataframes side by side on the supplied key, and perhaps using the supplied WHERE clause"""

    joined_df = df1.merge(df2, on=key, how=how)

    if where_clause is not None:
        joined_df = joined_df.query(where_clause)

    return joined_df
