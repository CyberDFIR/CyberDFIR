import requests
import os
from datetime import datetime

WATCHLIST_FILE = "watchlist.txt"
URL = "https://query1.finance.yahoo.com/v8/finance/chart/{}?interval=1d&range=1d"
HEADERS = {"User-Agent": "Mozilla/5.0"}


def read_watchlist(file_name):
    if not os.path.exists(file_name):
        print("file not found")
        return []

    symbols = []
    with open(file_name, "r") as file:
        for line in file:
            symbols.append(line.strip())

    return symbols


def execution_logger(func):
    def wrapper(self, symbol):
        time_now = datetime.now().strftime("%H:%M:%S")
        print(f"[{time_now}] Fetching data for: {symbol}...")
        return func(self, symbol)
    return wrapper



class StockClient:

    @execution_logger
    def fetch_price(self, symbol):
        try:
            response = requests.get(URL.format(symbol), headers=HEADERS)
            data = response.json()

            meta = data["chart"]["result"][0]["meta"]

            return {
                "Symbol": symbol,
                "Current Price": meta["regularMarketPrice"],
                "Previous Close": meta["chartPreviousClose"]
            }

        except:
            return None



