import pandas as pd
from viz import plot_total_sleep_each_day
from sleep_score import predict_sleepscore_v3, predict_sleepscore_v3
from weather import get_weather_data

SLEEP_FILE = "./data/SLEEP/SLEEP_1725530521869.csv"

def read_sleep_file():
    df = pd.read_csv(SLEEP_FILE, quotechar='"', escapechar='\\')
    return df

# for index, row in read_sleep_file().iterrows():
#     print(f"Row {index}")
#     print(f"Date {row['date']}")

### Predict sleep score with linear regression
# predict_sleepscore_v2(SCORE_PREDICTION_MODEL, {
#         "total_sleep_time": total_sleep_duration_min.tolist(),
#         "deep_time": df["deepSleepTime"].tolist() ,
#         "shallow_time": df["shallowSleepTime"].tolist() ,
#         "wake_time": df["wakeTime"].tolist(),
#         "rem_time": df["REMTime"].tolist(),
#     })

def merge_weather(sleep_df: pd.DataFrame, weather_df: pd.DataFrame):
    return sleep_df.merge(weather_df, how="left", on="date")

def viz(df: pd.DataFrame):
    # add total sleep time
    # total_sleep_duration_hrs = round((df["deepSleepTime"] + df["shallowSleepTime"] + df["REMTime"])/60, 2)
    total_sleep_duration_min = df["deepSleepTime"] + df["shallowSleepTime"] + df["REMTime"]
    df['total_sleep_duration_hrs']  = round(total_sleep_duration_min/60, 2)
    df['date'] = pd.to_datetime(df["date"]).dt.date
    df['dates'] = df["date"]
    df = merge_weather(df, get_weather_data())
    print(df)

    # clean dirty data
    df["sleep_score"] = predict_sleepscore_v3(
        total_sleep_duration_min,
        df["deepSleepTime"] ,
        df["shallowSleepTime"],
        df["REMTime"],
        df["wakeTime"],
    )

    filtered_df = df[df['total_sleep_duration_hrs'] > 2]
    plot_total_sleep_each_day(filtered_df)

print(viz(read_sleep_file()))
