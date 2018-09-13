import operator

from pandas import DataFrame


def hamming_distance_dataframe(str1: str, df: DataFrame, threshold: int, op: operator) -> DataFrame:
    edit_distance_passes_threshold = df.apply(lambda x: op(hamming_distance(str1, x), threshold))
    return edit_distance_passes_threshold.loc[edit_distance_passes_threshold == True]


def hamming_distance(str1: str, str2: str) -> int:
    diffs = 0
    if len(str1) < len(str2):
        str2 = str2[:len(str1)]
    elif len(str1) > len(str2):
        diffs += len(str1) - len(str2)
    else:
        pass
        # strings same length

    for ch1, ch2 in zip(str1, str2):
        if ch1 != ch2:
            diffs += 1

    return diffs