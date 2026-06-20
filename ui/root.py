from async_tkinter_loop.mixins import AsyncCTk
from customtkinter import CTk, CTkFrame, CTkLabel

from api import weather_api
from ui.components.input_card import InputCard
from ui.components.weather_card import WeatherCard
from ui.pages.error_page import ErrorPage
from ui.pages.loading_page import LoadingPage
from util.constants import Fonts
from util.score import calculate_score


class Root(CTk, AsyncCTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Main frame
        self.root_frame = CTkFrame(self)

        self.root_frame.rowconfigure(0, weight=1, uniform="wow")
        self.root_frame.rowconfigure(1, weight=20, uniform="wowe")
        self.root_frame.rowconfigure(2, weight=1, uniform="wowee")
        self.root_frame.columnconfigure((0, 1), weight=1, uniform="yes")

        self.root_frame.pack(expand=True, fill="both")

        # Left half
        self.left_half = CTkFrame(self.root_frame)
        self.left_half.grid(row=1, column=0, sticky="nsew", padx=(15, 0), pady=15)

        # Right Half
        self.right_half = CTkFrame(self.root_frame)
        self.right_half.grid(row=1, column=1, sticky="nsew", padx=15, pady=15)

        self.weather_card = WeatherCard(master=self.left_half)
        self.input_card = InputCard(master=self.right_half, guess_func=self.guess)

        self.link_inputs_to_weather_card()

    async def guess(self):
        # Retrieve info
        forecast = await weather_api.fetch_forecast()

        # Show loading
        self.show_loading_screen()

        # If no data retrieved then go to error page
        if not forecast:
            ErrorPage(self.root_frame)
            return

        # Remove old input card
        self.input_card.destroy()

        # Display left half Header
        CTkLabel(self.root_frame, text="Your Guess", font=Fonts.WEATHER_HEADER).grid(
            row=0, column=0, sticky="nsew", padx=(15, 0), pady=8
        )

        # Display right half Header
        CTkLabel(self.root_frame, text="Forecast", font=Fonts.WEATHER_HEADER).grid(
            row=0, column=1, sticky="nsew", padx=(15, 0), pady=8
        )

        # Generate a new card from forecast and set it to the right half
        WeatherCard(
            master=self.right_half,
            weather_type=forecast["weather_type"],
            min_temp=forecast["min_temp"],
            max_temp=forecast["max_temp"],
            rf_min=forecast["rf_min"],
            rf_max=forecast["rf_max"],
            uv_index=forecast["uv_index"],
        )

        # Calculate and display score
        guess = {
            "weather_type": self.input_card.weather_type_var.get().lower(),
            "min_temp": self.input_card.min_temp_var.get(),
            "max_temp": self.input_card.max_temp_var.get(),
            "rf_min": self.input_card.rf_min_temp_var.get(),
            "rf_max": self.input_card.rf_max_temp_var.get(),
            "uv_index": self.input_card.uv_index_var.get(),
        }

        score = calculate_score(guess, forecast)

        text_color = "white"
        if 0 <= score < 20:
            text_color = "red"
        elif 20 <= score < 40:
            text_color = "mild red"
        elif 40 <= score <= 60:
            text_color = "yellow"
        elif 60 <= score < 90:
            text_color = "green"
        else:
            text_color = "lime"

        CTkLabel(
            self.root_frame,
            text_color=text_color,
            font=Fonts.LOADING,
            text=f"Your Score : {round(number=score, ndigits=2)}%",
        ).grid(row=2, column=0, columnspan=2, sticky="nsew", padx=15, pady=(0, 15))

    def show_loading_screen(self):
        self.loading = LoadingPage(parent=self, transition_time_ms=5000)
        self.after(ms=5000, func=self.loading.destroy)

    def link_inputs_to_weather_card(self):
        self.input_card.weather_type_var.trace_add(
            mode="write",
            callback=lambda *args: self.weather_card.set_icon(
                self.input_card.weather_type_var.get().lower()
            ),
        )

        self.input_card.min_temp_var.trace_add(
            mode="write",
            callback=lambda *args: self.weather_card.min_temp.configure(
                text=f"Min Temp: {self.input_card.min_temp_var.get()}"
            ),
        )

        self.input_card.max_temp_var.trace_add(
            mode="write",
            callback=lambda *args: self.weather_card.max_temp.configure(
                text=f"Max Temp: {self.input_card.max_temp_var.get()}"
            ),
        )
        self.input_card.rf_min_temp_var.trace_add(
            mode="write",
            callback=lambda *args: self.weather_card.rf_min_temp.configure(
                text=f"Min Temp: {self.input_card.rf_min_temp_var.get()}"
            ),
        )

        self.input_card.rf_max_temp_var.trace_add(
            mode="write",
            callback=lambda *args: self.weather_card.rf_max_temp.configure(
                text=f"Max Temp: {self.input_card.rf_max_temp_var.get()}"
            ),
        )

        self.input_card.uv_index_var.trace_add(
            mode="write",
            callback=lambda *args: self.weather_card.uv_label.configure(
                text=f"UV Index: {self.input_card.uv_index_var.get()}"
            ),
        )
