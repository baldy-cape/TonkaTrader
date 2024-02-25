# tiingo.py

def get_tiingo_daily_stock_data (ticker, api_key, start_date, end_date):
    # API reference https://www.tiingo.com/documentation/end-of-day
    import requests
    import pandas as pd
    import json

    url = "https://api.tiingo.com/tiingo/daily/" + ticker + "/prices?token=" + api_key + "&startDate=" + start_date + "&endDate=" + end_date 
    response = requests.get(url)
    data = response.json()

    # Convert JSON data to pandas DataFrame
    if data:  # Ensure there's data to avoid errors
        df = pd.DataFrame(data)
        # Convert 'date' to datetime format and set as index
        df['date'] = pd.to_datetime(df['date'])
        df.set_index('date', inplace=True)
        return df
    else:
        return pd.DataFrame()  # Return an empty DataFrame if no data
