import requests
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(".env"))
api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")

symbol = "NVDA"
url = f"https://data.alpaca.markets/v2/stocks/{symbol}/bars/latest?feed=iex"

headers = {
    "accept": "application/json",
    "APCA-API-KEY-ID": api_key,
    "APCA-API-SECRET-KEY": api_secret,
}

response = requests.get(url, headers=headers)

print(response.text)
