"""
result = {
    "weather_type": get_weather_category(day_two["Day"]["Icon"]),
    "min_temp": temp["Minimum"]["Value"],
    "max_temp": temp["Maximum"]["Value"],
    "rf_min": rf["Minimum"]["Value"],
    "rf_max": rf["Maximum"]["Value"],
    "uv_index": day_two["AirAndPollen"][5]["Value"],
}
"""


def calculate_score(guess, forecast) -> float:

    weather_type_accuracy = (
        1 if guess["weather_type"] == forecast["weather_type"] else 0
    )

    min_temp_error = (
        abs(forecast["min_temp"] - guess["min_temp"]) / forecast["min_temp"]
    )
    min_temp_accuracy = max(0, 1 - min_temp_error)

    max_temp_error = (
        abs(forecast["max_temp"] - guess["max_temp"]) / forecast["max_temp"]
    )
    max_temp_accuracy = max(0, 1 - max_temp_error)

    rf_min_error = abs(forecast["rf_min"] - guess["min_temp"]) / forecast["rf_min"]
    rf_min_accuracy = max(0, 1 - rf_min_error)

    rf_max_error = abs(forecast["rf_max"] - guess["min_temp"]) / forecast["rf_max"]
    rf_max_accuracy = max(0, 1 - rf_max_error)

    uv_index_error = (
        abs(forecast["uv_index"] - guess["uv_index"]) / forecast["uv_index"]
    )
    uv_index_accuracy = max(0, 1 - uv_index_error)

    final_score = (
        weather_type_accuracy
        + min_temp_accuracy
        + max_temp_accuracy
        + rf_min_accuracy
        + rf_max_accuracy
        + uv_index_accuracy
    ) * 20  # for converting to %

    return final_score
