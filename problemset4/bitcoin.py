import sys

import requests

API_URL = "https://rest.coincap.io/v3/assets/bitcoin"
API_KEY = "50850981aaaf21a44dc5cd8cb734c6f554d0e15b03649f7cb943e020735562b0"


def main():
    amount = get_amount()
    data = fetch_bitcoin_data()
    print(data)  # explore the structure; using it with amount is up to you


def get_amount():
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    try:
        return float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")


def fetch_bitcoin_data():
    try:
        response = requests.get(API_URL, params={"apiKey": API_KEY}, timeout=10)
        response.raise_for_status()
        aux1 = response.json()
        aux2 = aux1['data']
        price = aux2['priceUsd']
        return price
    except requests.RequestException as e:
        sys.exit(f"Request failed: {e}")


if __name__ == "__main__":
    main()