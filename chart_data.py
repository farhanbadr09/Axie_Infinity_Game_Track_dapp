import requests
from datetime import datetime
def data():
    date_m = []
    url = "https://api.coingecko.com/api/v3/coins/smooth-love-potion/market_chart?vs_currency=usd&days=1"
    a = requests.get(url)
    b = a.json()
    b = b['prices']
    return b
print(data())




