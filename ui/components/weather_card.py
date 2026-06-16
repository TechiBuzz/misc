from customtkinter import *

class WeatherCard(CTkFrame):
    def __init__(self, master, weather_type, min_temp, max_temp):
        super().__init__(self, master)