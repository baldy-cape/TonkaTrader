def display_price_movement(data):
    # Calculate daily percent change and display
    data['Daily Change'] = (data['4. close'] - data['1. open']) / data['1. open'] * 100

    for index, row in data.iterrows():
        print(f"Date: {index}, Open: ${row['1. open']:.2f}, Close: ${row['4. close']:.2f}, Daily Change: {row['Daily Change']:.2f}%")

