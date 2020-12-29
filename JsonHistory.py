import json
import pandas as pd


class JsonHistory:

    def __init__(self, speed=0):
        self.isLoaded = False
        self.size = 0

    def load_dataframe_from_json(self, json_file):
        with open('data/'+json_file) as f:
            raw_data_from_json_file = json.load(f)
        if isinstance(raw_data_from_json_file, dict):
            value = raw_data_from_json_file["data"]
        else:
            value = raw_data_from_json_file
        historical_list_of_dicts = value
        dataframe_from_list_of_dictionaries = pd.DataFrame(historical_list_of_dicts)
        self.isLoaded = True
        self.size = len(dataframe_from_list_of_dictionaries.index)
        return dataframe_from_list_of_dictionaries

    def is_loaded(self):
        return self.isLoaded

    def get_size(self):
        return self.size


if __name__ == '__main__':
    json_history = JsonHistory()
    print("I'm a json_history!")
    df = json_history.load_dataframe_from_json('nest-egg-vanguard-config.json')
    print(json_history.is_loaded())
    print(json_history.get_size())
    minValue = df['year'].min()
    print("Sum: ", df["year"].sum())
    print("Mean: ", df["year"].mean())
    print("Median: ", df["year"].median())
    print("Maximum: ", df["year"].max())
    print("Minimum: ", df["year"].min())
