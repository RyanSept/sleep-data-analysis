import numpy as np
import pandas
from sklearn.linear_model import LinearRegression

# Training data
data = {
    "total_sleep_time": [552, 449, 539, 379, 349, 432, 546],
    "deep_time": [113, 104, 101, 74, 67, 82, 26],
    "shallow_time": [392, 344, 358, 236, 230, 231, 518],
    "wake_time": [47, 1, 5, 0, 7, 51, 2],
    "rem_time": [93, 52, 75, 69, 45, 68, 0],
    "score": [93, 83, 87, 82, 75, 78, 57],
}


def create_model():
    # Converting data to numpy arrays
    np_arrs = np.array(
        [
            data["total_sleep_time"],
            data["deep_time"],
            data["shallow_time"],
            data["wake_time"],
            data["rem_time"],
        ]
    ).T

    scores = np.array(data["score"])

    # Linear regression model to fit the data
    model = LinearRegression()
    model.fit(np_arrs, scores)

    # Coefficients of the model
    coefficients = model.coef_
    intercept = model.intercept_

    # Predicted scores based on the model
    predicted_scores = model.predict(np_arrs)
    print(coefficients, intercept, predicted_scores)

    return model


def predict_sleepscore(model, data):
    np_arrs = np.array(
        [
            data["total_sleep_time"],
            data["deep_time"],
            data["shallow_time"],
            data["wake_time"],
            data["rem_time"],
        ]
    ).T
    return model.predict(np_arrs)

def predict_sleepscore_v2(totalSleep: pandas.Series, deepSleep: pandas.Series, shallowSleep: pandas.Series, REM: pandas.Series, wake: pandas.Series):
    sleepScore = (
        30 * np.minimum(deepSleep / (0.20 * totalSleep), 1) +
        30 * np.minimum(REM / (0.3 * totalSleep), 1) +
        20 * np.minimum(shallowSleep / (0.6 * totalSleep), 1) +
        20 * (1 - np.minimum(wake / (0.3 * totalSleep), 1))
    )
    # iterate through each row and calculate the sleep score

    return np.maximum(0, np.minimum(sleepScore, 100))

def predict_sleepscore_v3(total_sleep: pandas.Series, deep_sleep: pandas.Series, shallow_sleep: pandas.Series, rem_sleep: pandas.Series, wake_time: pandas.Series):
    # Define the weights
    w_total = 0.3   # Total sleep time importance
    w_deep = 0.25   # Deep sleep importance
    w_rem = 0.2     # REM sleep importance
    w_shallow = 0.15  # Shallow sleep importance
    w_wake = 0.1    # Wake time penalty

    # Recommended sleep ranges (can be adjusted)
    target_sleep_time = 480  # 8 hours in minutes

    # Calculate the score components
    score_total = (total_sleep / target_sleep_time) * 100
    score_deep = (deep_sleep / total_sleep) * 100
    score_rem = (rem_sleep / total_sleep) * 100
    score_shallow = (shallow_sleep / total_sleep) * 100
    score_wake = (wake_time / total_sleep) * 100

    # Weighted sleep score (out of 100)
    sleep_score = (w_total * score_total + w_deep * score_deep + w_rem * score_rem + w_shallow * score_shallow) - (w_wake * score_wake)

    # baseline start
    sleep_score += 22

    # Ensure the score is between 0 and 100
    return np.maximum(0, np.minimum(100, sleep_score))

def example():
    new_data = {
        "total_sleep_time": [514],
        "deep_time": [105],
        "shallow_time": [333],
        "wake_time": [1],
        "rem_time": [75],
    }
    print(predict_sleepscore(create_model(), new_data))

SCORE_PREDICTION_MODEL = create_model()
