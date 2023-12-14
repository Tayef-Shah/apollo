import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(".env"))
api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")

from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockLatestQuoteRequest

client = StockHistoricalDataClient(api_key, api_secret)
params = StockLatestQuoteRequest(symbol_or_symbols="GLD")

quote = client.get_stock_latest_quote(params)
latest_ask_price = quote["GLD"].ask_price
print(latest_ask_price)
