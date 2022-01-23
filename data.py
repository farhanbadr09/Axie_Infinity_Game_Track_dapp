import requests
def register_ronin(ronin_id_):

    ronin_id = "0x"+ronin_id_
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
    average_slp = b['average']
    game_slp = b['claimableTotal']
    return total_slp,average_slp,game_slp
# print(register_ronin('fccea27d008fdb921f1190c9c6e70f7a13bec997'))