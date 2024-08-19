import requests, os, configparser
import pandas as pd
import json

def  _get_weather(lat, lon):
    url = "https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/" + str(lon) + "/lat/" + str(lat) + "/data.json"

    r = requests.get(url)

    # print("url:", r.url)
    # print("http code:", r.status_code)

    json_data = r.json()

    return json_data

def _save_weather(json_data, filename):
   
   with open(filename + ".json", "w") as outfile:
    json.dump(json_data, outfile) 

helsinki = _get_weather(60.317949, 24.949388)
_save_weather(helsinki, "helsinki")

tampere = _get_weather(61.414710, 23.603993)
_save_weather(tampere, "tampere")

