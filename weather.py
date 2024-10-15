import pandas as pd
import numpy as np
import json
# read the weather data in the data directory using the pandas library
# create a function called read_weather_file that returns the weather data

def get_weather_data():
    """
    🏛️ Historical Weather API _ Open-Meteo.com.html
    https://open-meteo.com/en/docs/historical-weather-api#latitude=38.7538&longitude=-9.2308&start_date=2024-05-15&end_date=2024-09-04&hourly=temperature_2m,relative_humidity_2m,apparent_temperature,soil_temperature_7_to_28cm
    Falagueira, Amadora, Portugal
    """
    # read json file using with open
    with open("./data/weather-data-2024-05-to-2024-09.json") as f:
        # return the data using the pandas library
        data = json.loads(f.read())

    df = pd.DataFrame(
        {
        "time": data["hourly"]["time"],
        "apparent_temperature": data["hourly"]["apparent_temperature"],
        "relative_humidity_2m": data["hourly"]["relative_humidity_2m"],
    })
    # transform time to datetime
    df["time"] = pd.to_datetime(df["time"], unit="s")
    return rollup_into_days(df)


def rollup_into_days(df: pd.DataFrame):
    """
    Roll up the weather data into daily averages, each average should be calculated from 8pm to 8am for that day
    """
    new_df = pd.DataFrame(columns=["date", "apparent_temperature", "relative_humidity_2m"])
    dates = df["time"].dt.date.unique()
    for date in dates:
        night_time_values = df[(df["time"].dt.date == date) & (df["time"].dt.hour >= 20)]
        next_day_values = df[(df["time"].dt.date == date + pd.Timedelta(days=1)) & (df["time"].dt.hour <= 8)]

        combined_values = pd.concat([night_time_values, next_day_values])

        mean_apparent_temperature = combined_values["apparent_temperature"].mean()
        mean_relative_humidity = combined_values["relative_humidity_2m"].mean()

        # add the new values to the new dataframe do not use append it is deprecated
        new_df.loc[len(new_df)] = {
            "date": date,
            "apparent_temperature": mean_apparent_temperature,
            "relative_humidity_2m": mean_relative_humidity,
        }
    return new_df




def example():
    df = get_weather_data()
    print(df)

