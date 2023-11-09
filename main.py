# main.py
from alpha_vantage.timeseries import TimeSeries
from datetime import datetime, timedelta
from stock_data import get_amazon_stock_data
from display import display_price_movement
import configparser

def main():
    config = configparser.ConfigParser()
    config.read('settings.cfg')
    
    api_key = config['AlphaVantage']['api_key']
    amazon_data = get_amazon_stock_data(api_key)
    display_price_movement(amazon_data)

if __name__ == "__main__":
    main()

