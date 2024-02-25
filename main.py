#!/usr/bin/env python3
"""
A toy stock trading program that uses machine learning to predict stock prices.
"""
from pprint import pprint
import ast
from datetime import datetime
from tonka_trader import load_settings_file, create_empty_df, fill_full_training_data

if __name__ == "__main__":
    settings = load_settings_file("settings.cfg")
    for key in settings["DEFAULT"]:
        print(key, settings["DEFAULT"][key])

    start_date = settings["DEFAULT"]["start_date"]
    end_date = datetime.now().strftime("%Y-%m-%d")  # today
    stocks = ast.literal_eval(settings["DEFAULT"]["stocks"])
    api_key = settings["DEFAULT"]["tiingo_key"]

    # create empty dataframe with all the data to be used for training
    full_training_data = create_empty_df(start_date, end_date, stocks)

    # fill full_training_data with stock data
    fill_full_training_data(full_training_data, start_date, end_date, stocks, api_key)

    pprint(full_training_data)
