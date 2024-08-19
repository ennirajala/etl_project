import requests, os, configparser
import pandas as pd
import json

def  _create_openweather_string(lat, lon):
    url = "https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/" + str(lon) + "/lat/" + str(lat) + "/data.json"
    return url

def _get_openweather(lat, lon):

    r = requests.get(_create_openweather_string(lat, lon))

    print("url:", r.url)
    print("http code:", r.status_code)

    json_data = r.json() 

    return json_data


def _json_to_csv(json_data, csv_name):

    weather_data = {
        "date":json_data["timeSeries"][0]["validTime"],
        "parameters":json_data["timeSeries"][0]["parameters"]
    }

    weather_data = pd.json_normalize(weather_data) 

    # Enni's path "/home/ennirajala/enni-sini/test2.csv"
    # Sini's path

    df = pd.DataFrame(weather_data)
    df.to_csv("/home/ennirajala/enni-sini/"+ csv_name +".csv", index=False)


helsinki = _get_openweather(60.317949, 24.949388)
_json_to_csv(helsinki, "helsinki")

tampere = _get_openweather(61.414710, 23.603993)
_json_to_csv(tampere, "tampere")