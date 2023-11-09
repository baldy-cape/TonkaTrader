# stock_data.py
from alpha_vantage.timeseries import TimeSeries
from datetime import datetime, timedelta

def get_amazon_stock_data(api_key):
    ts = TimeSeries(key=api_key, output_format='pandas')
    end_date = datetime.now()
    start_date = end_date - timedelta(days=90)  # 3 months ago
    symbol = 'AMZN'

    # Retrieve Amazon stock data for the last 3 months
    data, _ = ts.get_daily(symbol=symbol, outputsize='full')
    data = data[start_date.strftime('%Y-%m-%d'):end_date.strftime('%Y-%m-%d')]
    
    return data

