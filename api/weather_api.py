import json
import os

import httpx

from util.constants import get_weather_category


async def fetch_forecast() -> dict | None:
    async with httpx.AsyncClient() as client:
        response = await client.get(
            "https://dataservice.accuweather.com/forecasts/v1/daily/5day/204108?details=true&metric=true",
            headers={"Authorization": f"Bearer {os.environ.get('WEATHER_API_KEY')}"},
        )

        if response.status_code == 200:
            # Get the data
            result = response.json()

            # Ensure not null
            if not result:
                return

            # Dump to file
            try:
                with open("dumps/weather_data.json", "w") as file:
                    json.dump(result, file)
            except Exception as e:
                print(e)

            # Parse info of 2nd day and return
            day_two = result["DailyForecasts"][1]

            temp = day_two["Temperature"]
            rf = day_two["RealFeelTemperature"]

            result = {
                "weather_type": get_weather_category(day_two["Day"]["Icon"]),
                "min_temp": temp["Minimum"]["Value"],
                "max_temp": temp["Maximum"]["Value"],
                "rf_min": rf["Minimum"]["Value"],
                "rf_max": rf["Maximum"]["Value"],
                "uv_index": day_two["AirAndPollen"][5]["Value"],
            }

            return result

    return None
