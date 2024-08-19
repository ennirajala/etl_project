import requests, os, configparser
import pandas as pd
import json

geo_locations = {
    "tampere": (61.5, 23.8),
    "pori": (61.5, 21.8),
    "helsinki": (60.2, 24.9),
    "turku": (60.5, 22.3)
}

API_KEY = "2892ea72bd2c25aa007cc04b653790a4"

def  _create_openweather_string(lat, lon, appid):
    url = "https://api.openweathermap.org/data/2.5/weather?lat=" + str(lat) + "&lon=" + str(lon) + "&appid=" + appid
    return url

def _get_openweather(lat, lon, appid):

    r = requests.get(_create_openweather_string(lat, lon, appid))

    print("url:", r.url)
    print("http code:", r.status_code)

    json_data = r.json() 

    weather_data = {
        "weather": json_data["weather"][0],
        "main": json_data["main"],
        "visibility": json_data["visibility"],
        "wind": json_data["wind"],
        "clouds": json_data["clouds"]
    }

    weather_data = pd.json_normalize(weather_data) 

    df = pd.DataFrame(weather_data)
    df.to_csv("/home/ennirajala/my_project/airflow/dags/" + str(lon) + ".csv", index=False)

    return json_data

def _write_weather_log(lat, lon, appid):
    json_list = []

    for city in geo_locations:
        (lat, lon) = geo_locations[city]

        json_list.append(_get_openweather(lat, lon, appid))
    
    with open("weather_log.json", "w") as final:
        json.dump(json_list, final)

_write_weather_log(61.5, 23.8, API_KEY)