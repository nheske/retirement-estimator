import pytest


import pandas as pd
from pandas import DataFrame, read_json
from pandas.testing import (assert_frame_equal, assert_series_equal)


@pytest.fixture
def lines_json_df():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    return df.to_json(lines=True, orient="records")


def test_read_jsonl():
    # GH9180
    result = read_json('{"a": 1, "b": 2}\n{"b":2, "a" :1}\n', lines=True)
    expected = DataFrame([[1, 2], [1, 2]], columns=['a', 'b'])
    assert_frame_equal(result, expected)
