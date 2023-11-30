import requests
from sklearn.linear_model import LinearRegression
import numpy as np

# Replace the previous API with Alpha Vantage
def get_gold_prices(api_key):
    url = f"https://www.alphavantage.co/api/query?function=GOLD&apikey={api_key}&output=json&datatype=json"
    response = requests.get(url)

    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        try:
            data = response.json()
            # Extract the gold prices from the JSON response
            prices = [
                {'date': item['timestamp'], 'price': float(item['USD']['PRICE'])}
                for item in list(data['Time Series']['Gold (USD)'].values())
            ]
            return prices
        except ValueError as e:
            print(f"Error decoding JSON: {e}")
    else:
        print(f"Error: Unable to fetch gold prices. Status code: {response.status_code}")

    return []

def train_model(data):
    xs = np.array([[index] for index, _ in enumerate(data)])
    ys = np.array([item['price'] for item in data])

    model = LinearRegression()
    model.fit(xs, ys)

    return model

def predict_gold_price(model, input_data):
    input_data = np.array([[item] for item in input_data])
    result = model.predict(input_data)

    # OUTPUT
    print(result.flatten())

def main():
    # Replace with your Alpha Vantage API key
    api_key = "YOUR_API_KEY"

    gold_prices = get_gold_prices(api_key)

    if gold_prices:
        model = train_model(gold_prices)

        # Use the most recent gold price as input data
        input_data = [gold_prices[-1]['price']]

        predict_gold_price(model, input_data)

if __name__ == "__main__":
    main()
