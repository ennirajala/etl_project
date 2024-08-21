import requests, os, configparser
import pandas as pd
import json

# Get weather data with API as a JSON format
def  _get_weather(lat, lon):
    url = "https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/" + str(lon) + "/lat/" + str(lat) + "/data.json"

    r = requests.get(url)

    json_data = r.json()

    return json_data

# Save weather data as JSON file
def _save_weather(json_data, filename):
   
   with open(filename + ".json", "w") as outfile:
    json.dump(json_data, outfile) 

def _start_api():
    # Coordinates of the locations
    HKI_COORDS = [60.317949, 24.949388]
    TRE_COORDS= [61.414710, 23.603993]

    # Json files names
    hki_filename = "helsinki"
    tre_filename = "tampere"

    helsinki = _get_weather(HKI_COORDS[0], HKI_COORDS[1])
    _save_weather(helsinki, hki_filename)

    tampere = _get_weather(TRE_COORDS[0], TRE_COORDS[1])
    _save_weather(tampere, tre_filename)

    return hki_filename

#_start_api()
   

