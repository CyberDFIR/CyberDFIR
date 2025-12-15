

from stock_client import read_watchlist, StockClient
from report import report

WATCHLIST_FILE = "watchlist.txt"

if __name__ == "__main__":
    symbols = read_watchlist(WATCHLIST_FILE)
    client = StockClient()

    stock_data = []

    for symbol in symbols:
        result = client.fetch_price(symbol)
        if result:
            stock_data.append(result)

    report(stock_data)
