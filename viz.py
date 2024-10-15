import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



def plot_total_sleep_each_day(sleep_data):
    # Plotting the graph
    plt.figure(figsize=(10, 6))

    # sleep duration timeseries chart
    plt.subplot(2, 1, 1)
    plt.title("Total Sleep Duration Since May", fontsize=14)

    fig, parent_graph = plt.subplots()

    parent_graph.set_xlabel("Date", fontsize=12)

    # first graph of sleep duration
    # parent_graph.set_ylabel("Total Sleep Duration (hours)", fontsize=12, color="b")
    # parent_graph.set_yticks(np.arange(min(round(sleep_data["total_sleep_duration_hrs"], 0)), 11, 0.25))
    # parent_graph.plot(sleep_data["dates"], sleep_data["total_sleep_duration_hrs"], marker="o", color="b", linestyle="-")

    parent_graph.tick_params(axis='x', rotation=45)

    # second graph of sleep score
    sleep_score_graph = parent_graph.twinx()
    sleep_score_graph.set_ylabel("Sleep Score", fontsize=12, color="r")
    sleep_score_graph.plot(sleep_data["dates"], sleep_data["sleep_score"], marker="+", color="r", linestyle="-")

    # third graph of apparent temperature
    apparent_temperature_graph = parent_graph.twinx()
    apparent_temperature_graph.spines.right.set_position(("axes", 1.1))
    apparent_temperature_graph.set_ylabel("Apparent Temperature", fontsize=12, color="orange")
    apparent_temperature_graph.plot(sleep_data["dates"], sleep_data["apparent_temperature"], marker="*", color="orange", linestyle="-")

    # fourth graph of relative humidity
    relative_humidity_graph = parent_graph.twinx()
    relative_humidity_graph.spines.right.set_position(("axes", 1.2))
    relative_humidity_graph.set_ylabel("Relative humidity", fontsize=12, color="green")
    relative_humidity_graph.plot(sleep_data["dates"], sleep_data["relative_humidity_2m"], marker="v", color="green", linestyle="-")

    plt.xticks(sleep_data["date"][::3], rotation=45)
    plt.grid(True)

    # sleep quality timeseries chart
    # plt.subplot(2, 1, 2)
    # plt.plot(sleep_data["dates"], sleep_data["total_sleep_duration_hrs"], marker="o", color="b", linestyle="-")
    # plt.title("Total Sleep Duration Since May", fontsize=14)
    # plt.xlabel("Date", fontsize=12)
    # plt.ylabel("Total Sleep Duration (hours)", fontsize=12)
    # plt.xticks(sleep_data["date"][::3], rotation=45)
    # plt.yticks(np.arange(min(round(sleep_data["total_sleep_duration_hrs"], 0)), 11, 0.25))
    # plt.grid(True)

    # Show the plot
    plt.tight_layout()
    plt.show()

def example():
    # Generate random dates and total sleep time data
    dates = pd.date_range(start="2024-09-01", periods=10, freq='D')
    total_sleep_time = [452, 489, 513, 476, 402, 521, 539, 465, 492, 467]

    # Create the dataframe
    sleep_data = pd.DataFrame({
        "dates": dates,
        "total_sleep_duration_hrs": [round(t/60, 1) for t in total_sleep_time]
    })
    plot_total_sleep_each_day(sleep_data)

# example()
