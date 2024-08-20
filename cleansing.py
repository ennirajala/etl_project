import pandas as pd

fmi_df = pd.read_csv("fmi.csv")
smhi_df = pd.read_csv("smhi.csv")

# Clean the fmi dataframe
dropped_fmi = ["Maximum temperature [°C]",
               "Minimum temperature [°C]",
               "Maximum wind speed [m/s]",
               "Maximum gust speed [m/s]",
               ]
fmi_df = fmi_df.drop(dropped_fmi, axis=1)

fmi_df['Date'] = fmi_df['Year'].astype(str) +"-0"+ fmi_df['Month'].astype(str) +"-"+ fmi_df['Day'].astype(str)
fmi_df = fmi_df.drop(['Year', 'Month', 'Day'], axis=1)

fmi_df = fmi_df.reindex(columns=["Date",
                                 "Time [Local time]",
                                 "Observation station",
                                 "Average temperature [°C]",
                                 "Average relative humidity [%]",
                                 "Wind speed [m/s]",
                                 "Average wind direction [°]",
                                 "Precipitation [mm]",
                                 "Average air pressure [hPa]"])

fmi_df.rename(columns={"Time [Local time]": 'Time',
                   "Observation station": 'Location',
                   "Average temperature [°C]": "Temperature [°C]",
                   "Average relative humidity [%]":"Relative humidity [%]",
                   "Average wind direction [°]": "Wind direction [°]",
                   "Average air pressure [hPa]": "Air pressure [hPa]"
                   }, inplace=True)

fmi_df.to_csv("/home/ennirajala/enni-sini/fmi_cleaned.csv", index=False)

# Clean the smhi dataframe
dropped_smhi = ["vis",
                "tstm",
                "tcc_mean",
                "lcc_mean",
                "mcc_mean",
                "hcc_mean",
                "gust",
                "pmin",
                "pmax",
                "spp",
                "pcat",
                "Wsymb2",
                "pmedian"]
smhi_df = smhi_df.drop(dropped_smhi, axis=1)

smhi_df[['Date', 'Time']] = smhi_df['date'].str.split('T', n=1, expand=True)
smhi_df = smhi_df.drop(["date"], axis=1)

smhi_df = smhi_df.reindex(columns=["Date",
                                 "Time",
                                 "location",
                                 "t",
                                 "r",
                                 "ws",
                                 "wd",
                                 "pmean",
                                 "msl"])

smhi_df.rename(columns={"location": 'Location',
                   "t": "Temperature [°C]",
                   "r":"Relative humidity [%]",
                   "ws": "Wind speed [m/s]",
                   "wd": "Wind direction [°]",
                   "pmean": "Precipitation [mm]",
                   "msl": "Air pressure [hPa]"
                   }, inplace=True)

smhi_df.loc[0, 'Time'] = "10:00"
smhi_df.loc[1, 'Time'] = "10:00"

smhi_df.loc[0, 'Location'] = "Vantaa Helsinki-Vantaa airport"
smhi_df.loc[1, 'Location'] = "Pirkkala Tampere-Pirkkala airport"

smhi_df.to_csv("/home/ennirajala/enni-sini/smhi_cleaned.csv", index=False)
