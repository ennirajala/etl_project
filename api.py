import requests, os, configparser
import pandas as pd
import json

geo_locations = {
    # "tampere": (61.414710, 23.603993),
    "helsinki": (60.317949, 24.949388),
}


def  _create_openweather_string(lat, lon):
    url = "https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/" + str(lon) + "/lat/" + str(lat) + "/data.json"
    return url

def _get_openweather(lat, lon):

    r = requests.get(_create_openweather_string(lat, lon))

    print("url:", r.url)
    print("http code:", r.status_code)

    json_data = r.json() 

    return json_data


def _json_to_csv(json_data):

    weather_data = {
        "date": json_data["timeSeries"][0]
        # "percipitation": json_data["timeSeries"][0][0],
        # "visibility": json_data["visibility"],
        # "wind": json_data["wind"],
        # "clouds": json_data["clouds"]
    }

    weather_data = pd.json_normalize(weather_data) 

    df = pd.DataFrame(weather_data)
    df.to_csv("/home/sinivuor/my_project/wip/test2.csv", index=False)


test1 = _get_openweather(60.317949, 24.949388)
_json_to_csv(test1)