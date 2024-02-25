#!/usr/bin/env python3
from TonkaTrader import * 
from pprint import pprint
from datetime import datetime 
import ast

if __name__ == "__main__":
    settings = load_settings_file("settings.cfg")
    for key in settings['DEFAULT']:
        print(key, settings['DEFAULT'][key])
     
    start_date = settings['DEFAULT']["start_date"]
    end_date = datetime.now().strftime("%Y-%m-%d") # today
    stocks = ast.literal_eval(settings['DEFAULT']["stocks"])
    api_key = settings['DEFAULT']["tiingo_key"]

    # create empty dataframe with all the data to be used for training
    full_training_data = create_empty_df(start_date, end_date, stocks)

    # fill full_training_data with stock data
    fill_full_training_data(full_training_data, start_date, end_date, stocks, api_key)
    
    pprint(full_training_data)




    # Get stock information from Tiingo using API key
    #tiingo_key = settings['DEFAULT']['tiingo_key']
    #ticker = "AAPL"
    #start_date = settings['DEFAULT']['start_date']
    #stock = get_tiingo_daily_stock_data(ticker, tiingo_key, start_date)
    #pprint(stock)
