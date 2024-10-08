import pandas as pd
import json
import numpy as np
import os

def _harmonize_smhi_data():
    # Reads json files
    with open('helsinki.json', 'r') as f:
        helsinki_json = json.load(f)

    with open('tampere.json', 'r') as f:
        tampere_json = json.load(f)

    # Slice only the parts we need from json data
    date = helsinki_json["timeSeries"][0]["validTime"]
    parameters_hki = helsinki_json["timeSeries"][0]["parameters"]
    parameters_tre = tampere_json["timeSeries"][0]["parameters"]

    # Create lists for Pandas data frames columns(names) and rows(values)
    names = ["date", "location"]

    values_hki = []
    values_hki.append(date)
    values_hki.append("Helsinki")

    values_tre = []
    values_tre.append(date)
    values_tre.append("Tampere")
    
    # Iterate through parameters lists and append values to columns and rows lists
    for i in range(len(parameters_hki)):
        names.append(parameters_hki[i]["name"])
        values_hki.append(parameters_hki[i]["values"][0])
        values_tre.append(parameters_tre[i]["values"][0])

    # Create Pandas data frame and reindex it
    df = pd.DataFrame(np.array(values_hki).reshape(-1,len(values_hki)), columns=names)

    df.loc[-1] = values_tre
    df.index = df.index + 1

    df.to_csv("smhi.csv", index=False)
 
def _harmonize_fmi_data():
    # Create Pandas data frames from fmi's csv files
    fmi_hki_df = pd.read_csv("helsinki_met.csv")
    fmi_tre_df = pd.read_csv("tampere_met.csv")

    # Slice only the rows we need from Pandas data frame
    clean_hki_df = fmi_hki_df[fmi_hki_df['Time [Local time]'] == "10:00"]
    clean_tre_df = fmi_tre_df[fmi_tre_df['Time [Local time]'] == "10:00"]

    # Merge data from two locations into same Pandas data frame
    fmi_df = pd.concat([clean_hki_df, clean_tre_df], axis=0)
    
    # Create csv file for harmonized data
    fmi_df.to_csv("fmi.csv", index=False)

def _start_harmonizing():
    # Create csv file for harmonized data
    _harmonize_smhi_data()
    _harmonize_fmi_data()








