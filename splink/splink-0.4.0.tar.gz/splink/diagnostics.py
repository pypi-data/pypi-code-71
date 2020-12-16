from functools import reduce
from copy import copy
import warnings

from pyspark.sql.dataframe import DataFrame
from pyspark.sql.session import SparkSession
from .check_types import check_types


altair_installed = True
try:
    import altair as alt
except ImportError:
    altair_installed = False

hist_def_dict = {
    "$schema": "https://vega.github.io/schema/vega-lite/v4.8.1.json",
    "config": {
        "title": {"fontSize": 14},
        "view": {"continuousHeight": 300, "continuousWidth": 400},
    },
    "data": {"values": None},
    "height": 200,
    "mark": "bar",
    "title": "Histogram of splink scores",
    "width": 700,
    "encoding": {
        "tooltip": [{"field": "count_rows", "title": "count", "type": "quantitative"}],
        "x": {
            "axis": {"title": "splink score"},
            "bin": "binned",
            "field": "splink_score_bin_low",
            "type": "quantitative",
        },
        "x2": {"field": "splink_score_bin_high"},
        "y": {
            "field": "normalised",
            "type": "quantitative",
            "axis": {"title": "probability density"},
        },
    },
}


@check_types
def _calc_probability_density(
    df_e: DataFrame,
    spark: SparkSession,
    buckets=None,
    score_colname=None,
):

    """perform splink score histogram calculations / internal function

    Compute a histogram using the provided buckets.

        Args:
            df_e (DataFrame): A dataframe of record comparisons containing a
                splink score, e.g. as produced by the .... function
            spark (SparkSession): SparkSession object
            score_colname: is the score in another column? defaults to None
            buckets: accepts either a list of split points or an integer number that is used
                to create equally spaced split points.  It defaults to 100 equally
                spaced split points from 0.0 to 1.0

        Returns:
            (list) : list of rows of histogram bins for appropriate splink score variable ready to be plotted.
    """

    # if splits a list then use it. if None... then create default. if integer then create equal bins

    if isinstance(buckets, int) and buckets != 0:
        buckets = [(x / buckets) for x in list(range(buckets))]
    elif buckets == None:
        buckets = [(x / 100) for x in list(range(100))]

    # ensure 0.0 and 1.0 are included in histogram

    if buckets[0] != 0:
        buckets = [0.0] + buckets

    if buckets[-1] != 1.0:
        buckets = buckets + [1.0]

    # ensure bucket splits are in ascending order

    buckets.sort()

    # If score_colname is used then use that. if score_colname not used if tf_adjusted_match_prob exists it is used.
    # Otherwise match_probability is used or if that doesnt exit a warning is fired and function exits

    if score_colname:
        hist = df_e.select(score_colname).rdd.flatMap(lambda x: x).histogram(buckets)

    elif "tf_adjusted_match_prob" in df_e.columns:

        hist = (
            df_e.select("tf_adjusted_match_prob")
            .rdd.flatMap(lambda x: x)
            .histogram(buckets)
        )

    elif "match_probability" in df_e.columns:

        hist = (
            df_e.select("match_probability").rdd.flatMap(lambda x: x).histogram(buckets)
        )

    else:
        warnings.warn("Cannot find score column")

    # get bucket from and to points
    bin_low = hist[0]
    bin_high = copy(hist[0])
    bin_low.pop()
    bin_high.pop(0)
    counts = hist[1]

    rows = []
    for item in zip(bin_low, bin_high, counts):
        new_row = {
            "splink_score_bin_low": item[0],
            "splink_score_bin_high": item[1],
            "count_rows": item[2],
        }
        rows.append(new_row)

    for r in rows:
        r["binwidth"] = r["splink_score_bin_high"] - r["splink_score_bin_low"]
        r["freqdensity"] = r["count_rows"] / r["binwidth"]

    sumfreqdens = reduce(lambda a, b: a + b["freqdensity"], rows, 0)

    for r in rows:
        r["normalised"] = r["freqdensity"] / sumfreqdens

    return rows


def _create_probability_density_plot(data):
    """plot score histogram

    Args:
        data (list): A list of rows of histogram bins
            as produced by the _calc_probability_density function
    Returns:
        if altair is installed a plot. if altair is not installed
            then it returns the vega lite chart spec as a dictionary
    """

    hist_def_dict["data"]["values"] = data

    if altair_installed:
        return alt.Chart.from_dict(hist_def_dict)
    else:
        return hist_def_dict


def splink_score_histogram(
    df_e: DataFrame,
    spark: SparkSession,
    buckets=None,
    score_colname=None,
):

    """splink score histogram diagnostic plot public API function

    Compute a histogram using the provided buckets and plot the result.

    Args:
        df_e (DataFrame): A dataframe of record comparisons containing a splink score,
            e.g. as produced by the `get_scored_comparisons` function
        spark (SparkSession): SparkSession object
        score_colname : is the score in another column? defaults to None
        buckets : accepts either a list of split points or an integer number that is used to
            create equally spaced split points. It defaults to 100 equally spaced split points from 0.0 to 1.0
     Returns:
        if altair library is installed this function returns a histogram plot. if altair is not installed
        then it returns the vega lite chart spec as a dictionary
    """

    rows = _calc_probability_density(
        df_e, spark=spark, buckets=buckets, score_colname=score_colname
    )

    return _create_probability_density_plot(rows)
