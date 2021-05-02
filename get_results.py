import requests
import datetime
import json
import pandas as pd

def fetch(POST_CODE):
    # POST_CODE = "160036"
    # age = 52
    # Print details flag
    print_flag = 'Y'
    numdays = 7
    data=[]
    base = datetime.datetime.today()
    date_list = [base + datetime.timedelta(days=x) for x in range(numdays)]
    date_str = [x.strftime("%d-%m-%Y") for x in date_list]

    for INP_DATE in date_str:
        URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(
            POST_CODE, INP_DATE)
        response = requests.get(URL)
        if response.ok:
            resp_json = response.json()
            # print(json.dumps(resp_json, indent = 1))
            flag = False
            if resp_json["centers"]:
                print("Available on: {}".format(INP_DATE))
                if (print_flag == 'y' or print_flag == 'Y'):
                    for center in resp_json["centers"]:
                        for session in center["sessions"]:
                            print("\t", center["name"])
                            print("\t", center["block_name"])
                            print("\t Price: ", center["fee_type"])
                            print("\t Available Capacity: ", session["available_capacity"])
                            if (session["vaccine"] != ''):
                                print("\t Vaccine: ", session["vaccine"])
                            print("\n\n")

                            data.append([center["name"],center["block_name"],center["fee_type"],
                                         center['state_name'],center['district_name'],center['center_id'],
                                         session["available_capacity"],session['vaccine'],INP_DATE])

            else:
                print("No available slots on {}".format(INP_DATE))
                data.append(['','','','','','','',INP_DATE])
    df=pd.DataFrame()
    df['center name']=[i[0] for i in data]
    df['block name'] = [i[1] for i in data]
    df['fee type '] = [i[2] for i in data]
    df['state name']=[i[3] for i in data]
    df['district name']=[i[4] for i in data]
    df['center id'] = [i[5] for i in data]
    df['available capacity'] = [i[6] for i in data]
    df['vaccine type']=[i[7] for i in data]
    df['date']=[i[8] for i in data]
    return df
