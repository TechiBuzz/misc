from customtkinter import *
from PIL import Image

from util.constants import Fonts, Icons


class WeatherCard(CTkFrame):
    def __init__(
        self,
        master,
        weather_type="sunny",
        min_temp=0,
        max_temp=100,
        rf_min=0,
        rf_max=100,
        uv_index=5,
    ):
        super().__init__(master, corner_radius=16)

        # Make a 6 x 1 grid
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=3, uniform="A")
        self.rowconfigure((2, 4, 5), weight=2, uniform="B")
        self.rowconfigure((1, 3), weight=1, uniform="C")

        # Weather Icon
        self.icon = CTkLabel(
            master=self,
            text="",
            image=CTkImage(Image.open(Icons.SUNNY), size=(125, 125)),
            corner_radius=16,
        )
        self.icon.grid(column=0, row=0, sticky="nsew")

        # Temperature Label
        self.temp_label = CTkLabel(
            master=self,
            text="Temperature",
            corner_radius=100,
            font=Fonts.WEATHER_HEADER,
        )
        self.temp_label.grid(column=0, row=1, sticky="nsew")

        # Min and Max Temps
        self.temp_row = CTkFrame(master=self, corner_radius=16)
        self.temp_row.columnconfigure((0, 1), weight=1, uniform="D")
        self.temp_row.rowconfigure((0), weight=1)
        self.temp_row.grid(column=0, row=2, sticky="nsew")

        self.min_temp = CTkLabel(
            master=self.temp_row,
            text=f"Min Temp: {min_temp}C",
            font=Fonts.WEATHER_LABELS,
        )
        self.min_temp.grid(column=0, row=0, sticky="nsew")

        self.max_temp = CTkLabel(
            master=self.temp_row,
            text=f"Max Temp: {max_temp}C",
            font=Fonts.WEATHER_LABELS,
        )
        self.max_temp.grid(column=1, row=0, sticky="nsew")

        # RealFeel Temperature Label
        self.rf_temp_label = CTkLabel(
            master=self,
            text="RealFeel™",
            corner_radius=100,
            font=Fonts.WEATHER_HEADER,
        )
        self.rf_temp_label.grid(column=0, row=3, sticky="nsew")

        # Min and Max RF Temps
        self.rf_temp_row = CTkFrame(master=self, corner_radius=16)
        self.rf_temp_row.columnconfigure((0, 1), weight=1, uniform="E")
        self.rf_temp_row.rowconfigure((0), weight=1)
        self.rf_temp_row.grid(column=0, row=4, sticky="nsew")

        self.rf_min_temp = CTkLabel(
            master=self.rf_temp_row,
            text=f"Min Temp: {rf_min}C",
            font=Fonts.WEATHER_LABELS,
        )
        self.rf_min_temp.grid(column=0, row=0, sticky="nsew")

        self.rf_max_temp = CTkLabel(
            master=self.rf_temp_row,
            text=f"Max Temp: {rf_max}C",
            font=Fonts.WEATHER_LABELS,
        )
        self.rf_max_temp.grid(column=1, row=0, sticky="nsew")

        # UV Index Label
        self.uv_label = CTkLabel(
            master=self, text=f"UV Index: {uv_index}", font=Fonts.WEATHER_HEADER
        )
        self.uv_label.grid(column=0, row=5, sticky="nsew")

        self.pack(expand=True, fill="both", side="left", padx=5, pady=5)

    def set_icon(self, icon_type: str):
        img = Icons.desc_to_image.get(icon_type, Icons.SUNNY)
        self.icon.configure(image=CTkImage(Image.open(img), size=(125, 125)))
