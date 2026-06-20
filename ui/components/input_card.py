from tkinter import IntVar, StringVar

from async_tkinter_loop.async_tkinter_loop import async_handler
from customtkinter import CTkButton, CTkFrame, CTkLabel, CTkOptionMenu, CTkSlider
from customtkinter.windows.ctk_input_dialog import CTkEntry

from util.constants import Fonts


class InputCard(CTkFrame):
    def __init__(self, master, guess_func):
        super().__init__(master)

        # Variables
        self.weather_type_var = StringVar(value="Sunny")

        self.min_temp_var = IntVar(value=0)
        self.max_temp_var = IntVar(value=100)

        self.rf_min_temp_var = IntVar(value=0)
        self.rf_max_temp_var = IntVar(value=100)

        self.uv_index_var = IntVar(value=5)

        # Weather Type Selection
        self.weather_selection = CTkFrame(self)
        self.weather_selection.pack(expand=True, fill="both", padx=10, pady=(10, 0))

        self.weather_text = CTkLabel(
            self.weather_selection, text="Weather Type", font=Fonts.INPUT_DROPDOWN
        )
        self.weather_text.pack(expand=True, fill="both", padx=5, pady=5)

        self.weather_selection_dropdown = CTkOptionMenu(
            self.weather_selection,
            corner_radius=100,
            values=["Cloudy", "Rainy", "Snowy", "Sunny", "Thunderstorm"],
            variable=self.weather_type_var,
            font=Fonts.INPUT_DROPDOWN_SELECTED,
            dropdown_font=Fonts.INPUT_DROPDOWN,
            anchor="center",
        )
        self.weather_selection_dropdown.pack(expand=True, fill="both", padx=5, pady=5)

        # Temperature Selection
        self.temp_selection = CTkFrame(self)
        self.temp_selection.pack(expand=True, fill="both", padx=10, pady=(10, 0))

        """ Min temp stuff """
        self.min_temp_row = CTkFrame(self.temp_selection)
        self.min_temp_row.pack(expand=True, fill="both", padx=5, pady=5)

        self.min_temp_label = CTkLabel(
            self.min_temp_row, text="Minimum Temperature", font=Fonts.INPUT_DROPDOWN
        )
        self.min_temp_label.pack(expand=True, fill="both", padx=5, pady=5)

        self.min_temp_slider = CTkSlider(
            self.min_temp_row,
            from_=0,
            to=100,
            number_of_steps=100,
            variable=self.min_temp_var,
        )
        self.min_temp_slider.pack(expand=True, fill="both", padx=5, pady=5)

        self.min_temp_display = CTkEntry(
            self.min_temp_row,
            textvariable=self.min_temp_var,
            font=Fonts.INPUT_DROPDOWN,
            state="disabled",
        )
        self.min_temp_display.pack(expand=True, fill="both", padx=5, pady=5)

        """ Max temp stuff """
        self.max_temp_row = CTkFrame(self.temp_selection)
        self.max_temp_row.pack(expand=True, fill="both", padx=5, pady=5)
        self.max_temp_label = CTkLabel(
            self.max_temp_row, text="Maximum Temperature", font=Fonts.INPUT_DROPDOWN
        )
        self.max_temp_label.pack(expand=True, fill="both", padx=5, pady=5)

        self.max_temp_slider = CTkSlider(
            self.max_temp_row,
            from_=0,
            to=100,
            number_of_steps=100,
            variable=self.max_temp_var,
        )
        self.max_temp_slider.pack(expand=True, fill="both", padx=5, pady=5)

        self.max_temp_display = CTkEntry(
            self.max_temp_row,
            textvariable=self.max_temp_var,
            font=Fonts.INPUT_DROPDOWN,
            state="disabled",
        )
        self.max_temp_display.pack(expand=True, fill="both", padx=5, pady=5)

        # RF Temperature Selection
        self.rf_temp_selection = CTkFrame(self)
        self.rf_temp_selection.pack(expand=True, fill="both", padx=10, pady=(10, 0))

        """ RF Min temp stuff """
        self.rf_min_temp_row = CTkFrame(self.rf_temp_selection)
        self.rf_min_temp_row.pack(expand=True, fill="both", padx=5, pady=5)

        self.rf_min_temp_label = CTkLabel(
            self.rf_min_temp_row,
            text="RealFeel™  minimum Temperature",
            font=Fonts.INPUT_DROPDOWN,
        )
        self.rf_min_temp_label.pack(expand=True, fill="both", padx=5, pady=5)

        self.rf_min_temp_slider = CTkSlider(
            self.rf_min_temp_row,
            from_=0,
            to=100,
            number_of_steps=100,
            variable=self.rf_min_temp_var,
        )
        self.rf_min_temp_slider.pack(expand=True, fill="both", padx=5, pady=5)

        self.rf_min_temp_display = CTkEntry(
            self.rf_min_temp_row,
            textvariable=self.rf_min_temp_var,
            font=Fonts.INPUT_DROPDOWN,
            state="disabled",
        )
        self.rf_min_temp_display.pack(expand=True, fill="both", padx=5, pady=5)

        """ RF Max temp stuff """
        self.rf_max_temp_row = CTkFrame(self.rf_temp_selection)
        self.rf_max_temp_row.pack(expand=True, fill="both", padx=5, pady=5)

        self.rf_max_temp_label = CTkLabel(
            self.rf_max_temp_row,
            text="RealFeel™ Maximum Temperature",
            font=Fonts.INPUT_DROPDOWN,
        )
        self.rf_max_temp_label.pack(expand=True, fill="both", padx=5, pady=5)

        self.rf_max_temp_slider = CTkSlider(
            self.rf_max_temp_row,
            from_=0,
            to=100,
            number_of_steps=100,
            variable=self.rf_max_temp_var,
        )
        self.rf_max_temp_slider.pack(expand=True, fill="both", padx=5, pady=5)

        self.rf_max_temp_display = CTkEntry(
            self.rf_max_temp_row,
            textvariable=self.rf_max_temp_var,
            font=Fonts.INPUT_DROPDOWN,
            state="disabled",
        )
        self.rf_max_temp_display.pack(expand=True, fill="both", padx=5, pady=5)

        # UV Index
        self.uv_index_selection = CTkFrame(self)
        self.uv_index_selection.pack(expand=True, fill="both", padx=10, pady=(10, 0))

        """ UV Index stuff """
        self.uv_index_row = CTkFrame(self.uv_index_selection)
        self.uv_index_row.pack(expand=True, fill="both", padx=5, pady=5)

        self.uv_index_label = CTkLabel(
            self.uv_index_row,
            text="UV Index",
            font=Fonts.INPUT_DROPDOWN,
        )
        self.uv_index_label.pack(expand=True, fill="both", padx=5, pady=5)

        self.uv_index_slider = CTkSlider(
            self.uv_index_row,
            from_=0,
            to=15,
            number_of_steps=15,
            variable=self.uv_index_var,
        )
        self.uv_index_slider.pack(expand=True, fill="both", padx=5, pady=5)

        self.uv_index_display = CTkEntry(
            self.uv_index_row,
            textvariable=self.uv_index_var,
            font=Fonts.INPUT_DROPDOWN,
            state="disabled",
        )
        self.uv_index_display.pack(expand=True, fill="both", padx=5, pady=5)

        # Guess button
        self.button_frame = CTkFrame(self)
        self.button_frame.pack(expand=True, fill="both", padx=10, pady=10)

        self.guess_button = CTkButton(
            self.button_frame,
            text="GUESS",
            font=Fonts.WEATHER_HEADER,
            command=async_handler(guess_func),
        )
        self.guess_button.pack(expand=True, fill="both", padx=5, pady=5)

        # Instantly occupy parent
        self.pack(expand=True, fill="both", padx=5, pady=5)
