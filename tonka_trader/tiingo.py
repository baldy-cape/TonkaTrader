# tiingo.py
"""
Access Tiingo API to get stock data
"""

import requests
import pandas as pd


def get_tiingo_daily_stock_data(ticker, api_key, start_date, end_date):
    """
    Get daily stock data from Tiingo API
    """

    url = (
        "https://api.tiingo.com/tiingo/daily/"
        + ticker
        + "/prices?token="
        + api_key
        + "&startDate="
        + start_date
        + "&endDate="
        + end_date
    )
    response = requests.get(url, timeout=45)
    data = response.json()

    # Convert JSON data to pandas DataFrame
    dataframe = pd.DataFrame(data)
    # Convert 'date' to datetime format and set as index
    dataframe["date"] = pd.to_datetime(dataframe["date"])
    dataframe.set_index("date", inplace=True)
    return dataframe
