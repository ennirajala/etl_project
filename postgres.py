# The code presums a postgres connection on localhost

import os
import pandas as pd
import psycopg2 as ps  # postgres sql

from sqlalchemy import create_engine  # sql driver


CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))

def postgres_creator():  # sqlalchemy requires callback-function for connections
  return ps.connect(
        dbname="enni_sini",  # name of schema
        user="enni_sini",
        password="enni_sini",
        host="localhost",
        port="5432"
  )

postgres_engine = create_engine(
    url="postgresql+psycopg2://localhost",  # driver identification + dbms api
    creator=postgres_creator  # connection details
)

smhi_data = pd.read_csv(
    CURR_DIR_PATH + "/smhi_cleaned.csv",
    sep=",",
)

fmi_data = pd.read_csv(
    CURR_DIR_PATH + "/fmi_cleaned.csv",
    sep=",",
)


# Write to postgres
smhi_data.to_sql(name="smhi_data", con=postgres_engine, if_exists="replace", index=False)
fmi_data.to_sql(name="fmi_data", con=postgres_engine, if_exists="replace", index=False)
