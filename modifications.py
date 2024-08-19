import pandas as pd

def _json_to_csv(json_data, csv_name):

    weather_data = {
        "date":json_data["timeSeries"][0]["validTime"],
        "parameters":json_data["timeSeries"][0]["parameters"]
    }

    weather_data = pd.json_normalize(weather_data) 

    # Enni's path "/home/ennirajala/enni-sini/test2.csv"
    # Sini's path "/home/sinivuor/enni-sini/etl_project/tampere.csv"

    df = pd.DataFrame(weather_data)
    df.to_csv("/home/ennirajala/enni-sini/"+ csv_name +".csv", index=False)


data_list = []

