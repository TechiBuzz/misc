from async_tkinter_loop.mixins import AsyncCTk
from async_tkinter_loop import async_handler
from customtkinter import *

from api.weather import city_key


class Root(CTk, AsyncCTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.response_holder = CTkFrame(self)
        self.response_holder.pack(expand=True)

        self.label = CTkLabel(self.response_holder, text="NO DATA")
        self.label.pack()

        self.button = CTkButton(self, command=async_handler(lambda: self.fetch_city_code("Bengaluru")))
        self.button.pack(expand=True)

    async def fetch_city_code(self, city_name):
        self.button.configure(state="disabled")
        self.label.configure(text="Loading...")

        loading = CTkProgressBar(self.response_holder, mode="indeterminate")
        loading.pack(expand=True, fill="x")

        loading.start()

        # API call
        code = await city_key.get_city_location(city_name)

        if code:
            self.label.configure(text=code)
        else:
            self.label.configure(text="DIDNT GET ANYTHING :(")

        loading.stop()
        loading.pack_forget()

        self.button.configure(state="normal")