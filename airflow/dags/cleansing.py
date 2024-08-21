import pandas as pd

# Clenses fmi Pandas data frame
def _cleanse_fmi_data(fmi_df):
    # Drop columns that exist only in this fmi data
    dropped_fmi = ["Maximum temperature [°C]",
                "Minimum temperature [°C]",
                "Maximum wind speed [m/s]",
                "Maximum gust speed [m/s]",
                ]
    fmi_df = fmi_df.drop(dropped_fmi, axis=1)

    # Merge Year, Month and Day as a new Date column
    fmi_df['Date'] = fmi_df['Year'].astype(str) +"-0"+ fmi_df['Month'].astype(str) +"-"+ fmi_df['Day'].astype(str)
    fmi_df = fmi_df.drop(['Year', 'Month', 'Day'], axis=1)

    # Rearrange the columns to be in spesific order
    fmi_df = fmi_df.reindex(columns=["Date",
                                    "Time [Local time]",
                                    "Observation station",
                                    "Average temperature [°C]",
                                    "Average relative humidity [%]",
                                    "Wind speed [m/s]",
                                    "Average wind direction [°]",
                                    "Precipitation [mm]",
                                    "Average air pressure [hPa]"])

    # Rename the columns to have spesicif names
    fmi_df.rename(columns={"Time [Local time]": 'Time',
                    "Observation station": 'Location',
                    "Average temperature [°C]": "Temperature [°C]",
                    "Average relative humidity [%]":"Relative humidity [%]",
                    "Average wind direction [°]": "Wind direction [°]",
                    "Average air pressure [hPa]": "Air pressure [hPa]"
                    }, inplace=True)

    # Save clensed data as csv file
    fmi_df.to_csv("fmi_cleaned.csv", index=False)

# Clenses smhi Pandas data frame
def _cleanse_smhi_data(smhi_df):
    # Drop columns that exist only in this smhi data
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

    # Separate date column to be two new columns Date and Time
    smhi_df[['Date', 'Time']] = smhi_df['date'].str.split('T', n=1, expand=True)
    smhi_df = smhi_df.drop(["date"], axis=1)

    # Rearrange the columns to be in spesific order
    smhi_df = smhi_df.reindex(columns=["Date",
                                    "Time",
                                    "location",
                                    "t",
                                    "r",
                                    "ws",
                                    "wd",
                                    "pmean",
                                    "msl"])
    
    # Rename the columns to have spesicif names
    smhi_df.rename(columns={"location": 'Location',
                    "t": "Temperature [°C]",
                    "r":"Relative humidity [%]",
                    "ws": "Wind speed [m/s]",
                    "wd": "Wind direction [°]",
                    "pmean": "Precipitation [mm]",
                    "msl": "Air pressure [hPa]"
                    }, inplace=True)

    # Cleanse columns values to match fmi's data
    smhi_df.loc[0, 'Time'] = "10:00"
    smhi_df.loc[1, 'Time'] = "10:00"

    smhi_df.loc[0, 'Location'] = "Vantaa Helsinki-Vantaa airport"
    smhi_df.loc[1, 'Location'] = "Pirkkala Tampere-Pirkkala airport"

    # Save clensed data as csv file
    smhi_df.to_csv("smhi_cleaned.csv", index=False)

def _start_cleansing():
    # Read csv files as a Pandas data frame
    fmi_df = pd.read_csv("fmi.csv")
    smhi_df = pd.read_csv("smhi.csv")

    _cleanse_fmi_data(fmi_df)
    _cleanse_smhi_data(smhi_df)

