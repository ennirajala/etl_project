import pandas as pd
import json
import numpy as np

with open('helsinki.json', 'r') as f:
    helsinki_json = json.load(f)

with open('tampere.json', 'r') as f:
    tampere_json = json.load(f)

date = helsinki_json["timeSeries"][0]["validTime"]
parameters_hki = helsinki_json["timeSeries"][0]["parameters"]
parameters_tre = tampere_json["timeSeries"][0]["parameters"]

names = ["date", "location"]
values_hki = []
values_hki.append(date)
values_hki.append("Helsinki")

values_tre = []
values_tre.append(date)
values_tre.append("Tampere")

for i in range(len(parameters_hki)):
    names.append(parameters_hki[i]["name"])
    values_hki.append(parameters_hki[i]["values"][0])
    values_tre.append(parameters_tre[i]["values"][0])

df = pd.DataFrame(np.array(values_hki).reshape(-1,len(values_hki)), columns=names)

df.loc[-1] = values_tre
df.index = df.index + 1

# print(df)

# Enni's path: "/home/ennirajala/enni-sini/smhi.csv"
# Sini's path: "/home/sinivuor/enni-sini/etl_project/smhi"

df.to_csv("/home/sinivuor/enni-sini/etl_project/smhi.csv", index=False)
 






