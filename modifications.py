import pandas as pd
import json
import numpy as np

with open('helsinki.json', 'r') as f:
    helsinki_json = json.load(f)

date = helsinki_json["timeSeries"][0]["validTime"]
parameters = helsinki_json["timeSeries"][0]["parameters"]

names = ["date"]
values = []
values.append(date)

for i in range(len(parameters)):
    names.append(parameters[i]["name"])
    values.append(parameters[i]["values"][0])

df = pd.DataFrame(np.array(values).reshape(-1,len(values)), columns=names)
   
print(df)





