# helpers.py
"""
helper functions for the tonka_trader package.
"""
import configparser
import pandas as pd
from .tiingo import get_tiingo_daily_stock_data


def load_settings_file(filepath):
    """
    Load settings from a configuration file.

    Args:
        filepath (str): Path to the configuration file.

    Returns:
        configparser.ConfigParser: Parsed configuration settings.
    """
    config = configparser.ConfigParser()
    config.read(filepath)
    return config


def create_empty_df(start_date, end_date, stocks):
    """
    Create an empty dataframe with dates as index and stocks as columns.

    Args:
        start_date (str): Start date of the dataframe.
        end_date (str): End date of the dataframe.
        stocks (list): List of stocks to be used as columns.

    Returns:
        pandas.DataFrame: Empty dataframe with dates as index and stocks as columns.
    """

    dates = pd.date_range(start_date, end_date)
    return pd.DataFrame(index=dates, columns=stocks)


def fill_full_training_data(full_training_data, start_date, end_date, stocks, api_key):
    """
    populate the full_training_data dataframe with % change of adjOpen and adjClose for each
    stock in stocks
    """

    # for each stock  query triing API for raw sata and then populate the full_training_data
    # dataframe
    for stock in stocks:
        stock_data = get_tiingo_daily_stock_data(stock, api_key, start_date, end_date)
        # for each date in the stock_data, populate the full_training_data dataframe with %
        # change of adjOpen and adjClose
        for date in stock_data.index:
            full_training_data.loc[date, stock] = (
                (stock_data.loc[date, "adjClose"] - stock_data.loc[date, "adjOpen"])
                / stock_data.loc[date, "adjOpen"]
                * 100
            )
