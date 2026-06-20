import json

from async_tkinter_loop import async_handler
from async_tkinter_loop.mixins import AsyncCTk
from customtkinter import *
from PIL import Image

from api import weather_api


class Root(CTk, AsyncCTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.response_holder = CTkFrame(self)
        self.response_holder.pack(expand=True)

        self.label = CTkLabel(self.response_holder, text="NO DATA")
        self.label.pack()

        self.button = CTkButton(
            self,
            command=async_handler(lambda: self.fetch_weather("Bengaluru", 7)),
            text="Weathery Weather",
        )
        self.button.pack(expand=True)

    async def fetch_weather(self, city_name: str, days: int):
        self.button.configure(state="disabled")
        self.label.configure(text="Loading...")

        loading = CTkProgressBar(self.response_holder, mode="indeterminate")
        loading.pack(expand=True, fill="x")

        loading.start()

        # API calls
        weather_data = await weather_api.get_weather_info(city_name, days)

        if weather_data:
            with open("weather_data.json", "w") as file:
                json.dump(weather_data, file)

            self.label.configure(text="Got Weather Data")

            forecasts = weather_data["DailyForecasts"]
            for data in forecasts:
                datetime = data["Date"].partition("T")
                date = datetime[0]
                time = datetime[-1][:8]

                print("\n+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+")

                print(f"Date: {date}")
                print(f"Time: {time}")
                print(f"Min Temperature: {data['Temperature']['Minimum']['Value']}°C")
                print(f"Max Temperature: {data['Temperature']['Maximum']['Value']}°C")
                print(f"IconType: {data['Day']['IconPhrase']}")
                # print(f"Precipitation: {data['PrecipitationProbability']}%")

                print("+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+")
        else:
            self.label.configure(text="DIDNT GET ANYTHING :(")

        loading.stop()
        loading.pack_forget()

        self.button.configure(state="normal")
