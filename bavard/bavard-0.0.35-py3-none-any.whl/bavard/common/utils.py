from typing import Sequence

from sklearn.model_selection import StratifiedKFold
from sklearn.utils import shuffle as do_shuffle
import numpy as np


def leave_one_out(items: Sequence):
    """
    Cycles through `items`. On each ith item `item_i`, it yields
    `item_i`, as well as all items in `items` except `item_i` as a list.
    So given `items==[1,2,3,4]`, the first iteration will yield
    `1, [2,3,4]`, the second will yield `2, [1,3,4]`, and so on.
    """
    for i, item in enumerate(items):
        yield item, items[:i] + items[i + 1 :]


def make_stratified_folds(
    data: Sequence, labels: Sequence, nfolds: int, shuffle: bool = True, seed: int = 0
) -> tuple:
    """
    Takes `data`, a list, and breaks it into `nfolds` chunks. Each chunk is stratified
    by `labels`.
    """
    skf = StratifiedKFold(n_splits=nfolds, shuffle=shuffle, random_state=seed)
    fold_indices = [indices for _, indices in skf.split(data, labels)]
    folds = tuple([data[i] for i in indices] for indices in fold_indices)
    if shuffle:
        folds = tuple(do_shuffle(fold, random_state=seed) for fold in folds)
    return folds


def aggregate_dicts(dicts: list, agg: str) -> dict:
    """
    Aggregates a list of dictionaries all having the same keys.
    All values for a given key are aggregated into a single value
    using `agg`. Returns a single dictionary with the aggregated values
    """
    aggs = {
        "mean": np.mean,
        "stdev": np.std,
        "sum": np.sum,
        "median": np.median,
        "min": np.min,
        "max": np.max,
    }
    assert len(dicts) > 0
    keys = dicts[0].keys()
    result = {}
    for key in keys:
        values = [d[key] for d in dicts]
        if isinstance(values[0], dict):
            # Recurse
            result[key] = aggregate_dicts(values, agg)
        else:
            result[key] = aggs[agg](values, axis=0)
    return result
