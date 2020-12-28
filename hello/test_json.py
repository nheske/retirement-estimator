import pytest
import pandas as pd
import numpy as np
from pandas import DataFrame, read_json
from pandas.testing import (assert_frame_equal, assert_series_equal)
from Car import Car


# def test_car_brake():
#     car = Car(50)
#     car.brake()
#     assert car.speed == 45
#
#
# def test_read_jsonl():
#     result = read_json('{"a": 1, "b": 2}\n{"b":2, "a" :1}\n', lines=True)
#     expected = DataFrame([[1, 2], [1, 2]], columns=['a', 'b'])
#     assert_frame_equal(result, expected)


def test_read_json2():
    #list of lists to dataframe
    people_list_of_lists = [['Jon','Smith',21],['Mark','Brown',38],['Maria','Lee',42],['Jill','Jones',28],['Jack','Ford',55]]
    dataframe_from_list_of_dictionaries = DataFrame(people_list_of_lists, columns=['First_Name','Last_Name','Age'])
    print(dataframe_from_list_of_dictionaries)

    #list of dictionaries to dataframe
    data = [{"a": 1, "b": 2},
            {"a": 10, "b": 20}]
    dataframe_from_list_of_dictionaries = pd.DataFrame(data, index=['ind1', 'ind2'])
    print(dataframe_from_list_of_dictionaries)

    datab = [{"year": 1926, "stocks": 0.1163}, {"year": 1927, "stocks": 0.3744}]
    dataframe_from_list_of_dictionaries2 = pd.DataFrame(datab)
    print(dataframe_from_list_of_dictionaries2)

    dict_of_list_of_dict = read_json('{"data": [{"year": 1926, "stocks": 0.1163}, {"year": 1927, "stocks": 0.3744}]}')
    history = dict_of_list_of_dict['data']
    df3 = pd.DataFrame(history, index=['ind1', 'ind2'])
    print(df3)

    #     result = read_json({"data": [{"year": 1926,"stocks": 0.1163,"bonds": 0.0738,"cash": 0.032,"cpi": -0.0112},{"year": 1927,"stocks": 0.3744,"bonds": 0.0743,"cash": 0.031,"cpi": -0.0226}]}, lines=True)
#     result = read_json({"data": [{"year": 1926, "stocks": 0.1163}, {"year": 1927, "stocks": 0.3744}]}, lines=True)
    result = read_json('{"data": [{"year": 1926, "stocks": 0.1163}\n{"year":1927, "stocks" :0.3744}]}\n', lines=True)
    history2 = result.values[0]
    print(history2)
    history_df = pd.DataFrame(history2)
    expect = DataFrame([[[1926, 0.1163], [1927, 0.3744]]], columns=['year', 'stocks'])
    print(expect)

    df = pd.DataFrame(np.random.randn(5,3),columns=list('ABC'))
    print(df)
    val = df.values[0]
    print(val)
    exp = pd.DataFrame.from_dict(result)
    print(exp)

    expected = DataFrame([[[1926, 0.1163], [1927, 0.3744]]], columns=['year', 'stocks'])

    assert_frame_equal(result, expected)


def test_read_jsongood():
#     result = read_json({"data": [{"year": 1926,"stocks": 0.1163,"bonds": 0.0738,"cash": 0.032,"cpi": -0.0112},{"year": 1927,"stocks": 0.3744,"bonds": 0.0743,"cash": 0.031,"cpi": -0.0226}]}, lines=True)
#     result = read_json({"data": [{"year": 1926, "stocks": 0.1163}, {"year": 1927, "stocks": 0.3744}]}, lines=True)
    result = read_json('{"year": 1926, "stocks": 0.1163}\n{"year":1927, "stocks" :0.3744}\n', lines=True)
    expected = DataFrame([[1926, 0.1163], [1927, 0.3744]], columns=['year', 'stocks'])
    assert_frame_equal(result, expected)