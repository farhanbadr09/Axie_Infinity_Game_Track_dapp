def get_slp_rapid():
    import requests
    ronin_id = "0x"+'fccea27d008fdb921f1190c9c6e70f7a13bec997'
    url = "https://axie-infinity.p.rapidapi.com/get-update/"+ronin_id
    querystring = {"id": ronin_id}
    headers = {
        'x-rapidapi-host': "axie-infinity.p.rapidapi.com",
        'x-rapidapi-key': "da2ffd9f08msh2f8e980d67980c9p1334ebjsnc1775cf74c04"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    results = response
    re = results.json()
    b = re['slp']
    total_slp = str(b['total'])
    # average_slp = b['average']
    # game_slp = b['claimableTotal']
    # print(re)
    return total_slp
a = get_slp_rapid()
a = int(a)
print(a)
investor = 20
manager = 10
jackpot = 20
affiliate = 15
in_per = a *investor/100
ma_per = a *manager/100
ja_per = a *jackpot/100
af_per = a *affiliate/100


