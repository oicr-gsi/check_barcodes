from pathlib import Path

import pandas as pd
from pandas import DataFrame
from loaders import config


def getpath(file_path_string: str) -> Path:
    path = Path(file_path_string)
    path = path.expanduser()
    return path


def load_file_provenance(fpr_path: str, filters=None) -> DataFrame:
    fpr_path = getpath(fpr_path)

    # check if fpr has header
    first_record = pd.read_csv(fpr_path, delimiter='\t', nrows=1, header=None)
    if first_record.iloc[0, 0] == 'Last Modified':
        header_mode = 0
    else:
        header_mode = None

    fpr_iter = pd.read_csv(fpr_path, delimiter='\t', names=config.fpr_cols.keys(), dtype=config.fpr_cols,
                           header=header_mode, low_memory=False, iterator=True, chunksize=10000)
    fpr = pd.concat([fpr_chunk for fpr_chunk in fpr_iter])

    return fpr