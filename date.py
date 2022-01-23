import requests
from datetime import datetime
def data():
    date_m = []
    url = "https://api.coingecko.com/api/v3/coins/smooth-love-potion/market_chart?vs_currency=usd&days=1"
    a = requests.get(url)
    b = a.json()
    b = b['prices']
    # m = [str(a[0]) for a in b]
    # date_m = []
    # for i in m:
    #     timestamp = i[0:10]
    #     dt = datetime.fromtimestamp(int(timestamp))
    #     da = str(dt)
    #     hg = da[0:]
    #     date_m.append(hg)

    # n = [a[1] for a in b]
    # a_zip = zip(date_m, n)
    # zipped_list = list(a_zip)
    # data = []
    # for i in zipped_list:
    #     a = list(i)
    #     data.append(a)
    return b


print(data())