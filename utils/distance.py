import itertools
import operator

from pandas import DataFrame


def barcode_distance_dataframe(target: str, others: DataFrame, threshold: int, op: operator) -> DataFrame:
    barcode_distance_passes_threshold = others.apply(lambda other: op(barcode_distance(target, other), threshold))
    return barcode_distance_passes_threshold.loc[barcode_distance_passes_threshold == True]


def barcode_distance(target: str, other: str, barcode_separator='-') -> int:
    return sum([hamming_distance(target, other) for target, other in
                itertools.zip_longest(target.split(barcode_separator), other.split(barcode_separator), fillvalue='')])


def hamming_distance(target: str, other: str) -> int:
    diffs = 0
    if len(target) < len(other):
        other = other[:len(target)]
    elif len(target) > len(other):
        diffs += len(target) - len(other)
    else:
        pass
        # strings same length

    for ch1, ch2 in zip(target, other):
        if ch1 != ch2:
            diffs += 1

    return diffs
