import pandas as pd
import json
from pandas.testing import assert_frame_equal

import unittest


class MyTestCase(unittest.TestCase):

    if __name__ == '__main__':
        unittest.main()


def test_data_frames():
    fruits = ['apples', 'bananas', 'grapefruit', 'cherry', 'blueberry', 'orange', 'lemon']
    df = pd.DataFrame(fruits)

    df = pd.DataFrame(fruits, index=['a', 'b', 'c', 'd', 'e', 'f', 'g'], columns=['Names'])
    print(df)

    names = [['tom', 25], ['krish', 30], ['nick', 26], ['juli', 22]]
    df = pd.DataFrame(names, columns=['Name', 'Age'])
    print(df)

    multi_list_students = [['tom', 'reacher', 25, 'BS'], ['krish', 'pete', 30, 'PhD'],['nick', 'wilson', 26, 'MBA'], ['juli', 'williams', 22, 'GED']]
    df = pd.DataFrame(multi_list_students, columns=['First Name', 'Last Name', 'Age', 'Degree'], dtype=float)
    print(df)

    # list of name, degree, score
    nme = ["Tom", "Steve", "Rachel", "Pirom"]
    deg = ["MBA", "BCA", "M.Tech", "MBA"]
    scr = [90, 40, 80, 98]
    # dictionary of lists
    dict = {'name': nme, 'degree': deg, 'score': scr}
    df = pd.DataFrame(dict)
    print(df)


def test_data_frames_csv():
    cars = {'Brand': ['Honda Civic','Toyota Corolla','Ford Focus','Audi A4'], 'Price': [22000,25000,27000,35000], 'Year': [2015,2013,2018,2018]}
    df = pd.DataFrame(cars, columns= ['Brand', 'Price', 'Year'])
    df.to_csv (r'data/cars.csv', index = False, header=True)
    print(df)
    print()
    df = pd.read_csv(r'data/cars.csv')
    df.sort_values(by=['Brand'], inplace=True)
    print (df)

    #JSON file into Pandas DataFrame
    # reading the file yields data {'year': 1926, 'stocks': 0.1163, 'bonds': 0.07...  {'year': 1927, 'stocks': 0.3744, 'bonds': 0.07... }
    data = pd.read_json(r'data/sample.json')

    # displaying the DataFrame
    print(data.head(5))


def test_data_frames_lists():
    # list of lists to dataframe
    people_list_of_lists = [['Jon', 'Smith', 21], ['Mark', 'Brown', 38], ['Maria', 'Lee', 42], ['Jill', 'Jones', 28],
                            ['Jack', 'Ford', 55]]
    dataframe_from_list_of_lists = pd.DataFrame(people_list_of_lists, columns=['First_Name', 'Last_Name', 'Age'])
    print(dataframe_from_list_of_lists)

    # list of dictionaries to dataframe
    list_of_dictionaries = [{"year": 1926, "stocks": 0.1163}, {"year": 1927, "stocks": 0.3744}]
    dataframe_from_list_of_dictionaries = pd.DataFrame(list_of_dictionaries)
    print(dataframe_from_list_of_dictionaries)

    # list of 1 dictionary (key = "data") of a list of 2 dictionaries
    raw_data = [{"data": [{"year": 1926, "stocks": 0.1163}, {"year": 1927, "stocks": 0.3744}]}]
    dict1 = raw_data[0]
    historical_list_of_dicts = dict1["data"]
    dataframe_from_list_of_dictionaries3 = pd.DataFrame(historical_list_of_dicts)
    print(dataframe_from_list_of_dictionaries3)


def test_data_frames_json():
    with open('data/sample.json') as file:
        raw_data_from_json_file = json.load(file)
    historical_list_of_dicts = raw_data_from_json_file["data"]
    dataframe_from_list_of_dictionaries3 = pd.DataFrame(historical_list_of_dicts)
    print(dataframe_from_list_of_dictionaries3)


def test_read_jsonl():
    result = pd.read_json('{"a": 1, "b": 2}\n{"b":2, "a" :1}\n', lines=True)
    expected = pd.DataFrame([[1, 2], [1, 2]], columns=['a', 'b'])
    assert_frame_equal(result, expected)

