from flask import Flask,render_template,request,send_file
import requests
import json
from chart_data import data
import requests
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')


def collect_ronin():
    scholars_ronin_id = []
    users_ronin_id = []
    file = open('scholar.json',)
    data = json.load(file)
    scholars = data['scholars']
    for scholar in scholars:
        scholars_ronin_id.append(scholar['scholar_ronin'])

    file = open('data.json',)
    data = json.load(file)
    users = data['events']
    for user in users:
        users_ronin_id.append(user['user_ronin_id'])
    # print("scholars_ronin_id",scholars_ronin_id)
    # print("users_ronin_id",users_ronin_id)


global name
@app.route("/investorsighnup", methods=['GET','POST'])
def investorsighnup():
    global user_ronin_id
    user_ronin_id = ""
    if request.method == 'POST':
        email = request.form['email']
        name = request.form['name']
        password = request.form['password']
        ronin_id = request.form['currency']
        
        data_dict = {"user_name":name,
                    "user_email":email,
                    "user_password":password,
                    "user_ronin_id":ronin_id}

        user_ronin_id+=ronin_id

        with open('data.json','r+') as file:
            file.seek(0)
            data_json = json.load(file)
            file.seek(0)
            data_json["events"].append(data_dict)
            json.dump(data_json, file)
            file.close()
        print(ronin_id)

        return render_template('investorsighnup.html',d = data_dict )
    
    return render_template('investorsighnup.html')


def slp_chart_data_fun():
    slp_data_url = "https://api.coingecko.com/api/v3/coins/smooth-love-potion/market_chart?vs_currency=usd&days=1"
    slp_data_response = requests.get(slp_data_url)
    slp_data_json = slp_data_response.json()
    slp_chart_data = slp_data_json['prices']
    return slp_chart_data

def axie_infinity_chart_data_fun():
    axie_infinity_data_url = "https://api.coingecko.com/api/v3/coins/axie-infinity/market_chart?vs_currency=usd&days=1"
    axie_infinity_data_response = requests.get(axie_infinity_data_url)
    axie_infinity_data_json = axie_infinity_data_response.json()
    axie_infinity_chart_data = axie_infinity_data_json['prices']
    return axie_infinity_chart_data

def get_slp_rapid():
    ronin_id = "0x"+user_ronin_id
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

def slp_and_axie_infinity_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=smooth-love-potion&vs_currencies=usd"
    response = requests.get(url)
    re = response.json()
    slp_token = re['smooth-love-potion']
    slp_token_price = slp_token['usd']
    return slp_token_price

def slp_price_to_usd():
    price_slp = slp_and_axie_infinity_price()
    get_slp_attributes = get_slp_rapid()
    total_slp_usd = float(int(get_slp_attributes[0])) * float(price_slp)
    average_slp_usd = float(int(get_slp_attributes[1])) * float(price_slp)
    game_slp_usd = float(int(get_slp_attributes[2])) * float(price_slp)
    return str(total_slp_usd), str(average_slp_usd), str(game_slp_usd)

def scholar_data_view():
    file = open('scholar.json',)
    data = json.load(file)
    scholars = data['scholars']
    return scholars





@app.route("/ronin_user" , methods=['POST', 'GET'])
def ronin_user():    
    if request.method == 'POST':
        scholar_name = request.form['scholar_name']
        scholar_ronin = request.form['scholar_ronin']
        scholar_share = request.form['scholar_share']
        jackpot_share = request.form['jackpot_share']
        investor_share = request.form['investor_share']
        investor_name = request.form['investor_name']
        affiliate_share = request.form['affiliate_share']
        affiliate_name = request.form['affiliate_name']
        manager_share = request.form['manager_share']
        manager_name = request.form['manager_name']
        scholar_data = {"scholar_name":scholar_name,"scholar_ronin":scholar_ronin,"scholar_share":scholar_share,"jackpot_share":jackpot_share,"investor_share":investor_share,"investor_name":
                        investor_name,"affiliate_share":affiliate_share,"affiliate_name":affiliate_name,"manager_share":manager_share,"manager_name":manager_name}
        
        ronin_id = "0x"+scholar_ronin
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
        scholar_total_slp = str(b['total'])
        scholar_average_slp = b['average']
        scholar_game_slp = b['claimableTotal']
        # Calculate Stackholders Share
        total_slp_to_share = get_slp_rapid()
        total_slp_to_share = total_slp_to_share[0]
        total_slp_to_share = int(total_slp_to_share)

        investor_percentage = investor_share
        manager_percentage = manager_share
        jackpot_percentage = jackpot_share
        affiliate_percentage = affiliate_share
        scholar_percentage = scholar_share
        investor_percentage_value   =   total_slp_to_share * int(investor_percentage) / 100
        manager_percentage_value    =   total_slp_to_share * int(manager_percentage) / 100
        jackpot_percentage_value    =   total_slp_to_share * int(jackpot_percentage) / 100
        affiliate_percentage_value  =   total_slp_to_share * int(affiliate_percentage) / 100
        scholar_percentage_value    =   total_slp_to_share * int(scholar_percentage) / 100

        scholar_dict = {"scholar_name":scholar_name,
                    "scholar_ronin":scholar_ronin,
                    "scholar_share": scholar_percentage_value,
                    "jackpot_share":jackpot_percentage_value,
                    "investor_share":investor_percentage_value,
                    "investor_name":investor_name,
                    "affiliate_share":affiliate_percentage_value,
                    "affiliate_name":affiliate_name,
                    "manager_share":manager_percentage_value,
                    "manager_name":manager_name,
                    "scholar_total_slp":scholar_total_slp,
                    "scholar_average_slp":scholar_average_slp,
                    "scholar_game_slp":scholar_game_slp}
        with open('scholar.json','r+') as file:
            file.seek(0)
            data_json = json.load(file)
            file.seek(0)
            data_json["scholars"].append(scholar_dict)
            json.dump(data_json, file)
            file.close()

    slp_chart_data_obj = slp_chart_data_fun()
    axie_infinity_data_obj = axie_infinity_chart_data_fun()
    get_slp = get_slp_rapid()
    slp_to_usd_param = slp_price_to_usd()
    total_slp_to_usd = slp_to_usd_param[0]
    average_slp_to_usd = slp_to_usd_param[1]
    game_slp_to_usd = slp_to_usd_param[2]
    scholar_data_vie = scholar_data_view()
    
    return render_template('dashboard/index.html',slp_chart_data=slp_chart_data_obj, axie_infinity_data=axie_infinity_data_obj,total_slp = get_slp[0],game_slp = get_slp[2], average_slp = get_slp[1],total_slp_to_usd =total_slp_to_usd,average_slp_to_usd=average_slp_to_usd,game_slp_to_usd=game_slp_to_usd,scholar_data_view = scholar_data_vie)
 
    # return render_template('dashboard/index.html',slp_chart_data=slp_chart_data_obj, axie_infinity_data=axie_infinity_data_obj,total_slp = get_slp[0],game_slp = get_slp[2], average_slp = get_slp[1],total_slp_to_usd =total_slp_to_usd,average_slp_to_usd=average_slp_to_usd,game_slp_to_usd=game_slp_to_usd,scholar_data_view = scholar_data_vie,investor_percentage_value = investor_percentage_value,scholar_percentage_value = scholar_percentage_value, jackpot_percentage_value =  jackpot_percentage_value, affiliate_percentage_value = affiliate_percentage_value, manager_percentage_value = manager_percentage_value)

@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        file = open('data.json',)
        data = json.load(file)
        scholars = data['events']
        for i in scholars:
            if i["user_email"]  == email and i["user_password"] == password:
                slp_chart_data_obj = slp_chart_data_fun() 
                axie_infinity_data_obj = axie_infinity_chart_data_fun()
                scholar_data_vie = scholar_data_view()
                from data import register_ronin
                register_ronin_slp = register_ronin(i['user_ronin_id'])
                price_slp = slp_and_axie_infinity_price()

                total_slp_to_usd = float(int(register_ronin_slp[0]) * price_slp)
                average_slp_to_usd = float(int(register_ronin_slp[1]) * price_slp)
                game_slp_to_usd = float(int(register_ronin_slp[2]) * price_slp)

        
                return render_template("dashboard/index.html", slp_chart_data = slp_chart_data_obj,axie_infinity_data = axie_infinity_data_obj,scholar_data_view = scholar_data_vie,total_slp = register_ronin_slp[0],game_slp = register_ronin_slp[2],average_slp = register_ronin_slp[1],game_slp_to_usd = game_slp_to_usd, total_slp_to_usd = total_slp_to_usd,average_slp_to_usd = average_slp_to_usd)

    return render_template("affiliate-sign-in.html")



@app.route("/download")
def download():
    # Python program to convert
    # JSON file to CSV


    import json
    import csv


    # Opening JSON file and loading the data
    # into the variable data
    with open('scholar.json') as json_file:
        data = json.load(json_file)

    employee_data = data['scholars']

    # now we will open a file for writing
    data_file = open('data_file.csv', 'w')

    # create the csv writer object
    csv_writer = csv.writer(data_file)

    # Counter variable used for writing
    # headers to the CSV file
    count = 0

    for emp in employee_data:
        if count == 0:

            # Writing headers of CSV file
            header = emp.keys()
            csv_writer.writerow(header)
            count += 1

        # Writing data of CSV file
        csv_writer.writerow(emp.values())

    data_file.close()
    b = "data_file.csv"

    return send_file(b)



@app.route("/dashboard" , methods=['POST', 'GET'])
def test():
    if request.method == 'POST':
        name = request.form['name']
        print("Be Happy Farhan, Allah is with us",str(name))
    return render_template("dashboard/test.html")

@app.route("/abc")
def abc():
    return render_template("charts/chart.html",b = data())
    
app.run(debug=True)
