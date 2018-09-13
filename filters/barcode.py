import operator

import pandas as pd
from dask import dataframe as dd
from pandas import DataFrame

from utils.distance import hamming_distance_dataframe


def compare_barcodes(df_subset, df2_all, threshold, op):
    # remove subset from all
    df2_all_except_subset = df2_all.loc[~df2_all.index.isin(df_subset.index)]  # type: DataFrame

    if (df2_all_except_subset.empty):
        return pd.Series(index=df2_all_except_subset)
    else:
        return df_subset.apply(
            lambda x: pd.Series({'collisions':
                                     hamming_distance_dataframe(x, df2_all_except_subset, threshold,
                                                                op).index.tolist()}))


def get_collisions(df: DataFrame, threshold: int, op=operator.lt):
    df = dd.from_pandas(df, npartitions=32)
    collisions = df.groupby('Lane Name').apply(
        lambda records_by_lane: records_by_lane.groupby('Workflow Run SWID').apply(
            lambda records_by_lane_and_workflow_run: compare_barcodes(records_by_lane_and_workflow_run['IUS Tag'],
                                                                      records_by_lane['IUS Tag'],
                                                                      threshold,
                                                                      op))
        , meta=({'collisions': 'object'})
    )
    collisions = collisions.compute(scheduler='processes')
    collisions.reset_index(level=0, drop=True, inplace=True)

    return collisions[collisions['collisions'].apply(lambda x: len(x) > 0)]
