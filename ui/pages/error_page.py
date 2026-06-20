from customtkinter import CTkFrame, CTkLabel

from util.constants import Fonts


class ErrorPage(CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Widgets
        self.central_frame = CTkFrame(self, corner_radius=15)
        self.central_frame.place(
            relx=0.5, rely=0.5, relheight=0.93, relwidth=0.95, anchor="center"
        )

        self.text = CTkLabel(
            self.central_frame, text="An Error Occurred :(", font=Fonts.LOADING
        )
        self.text.pack(expand=True, fill="both")

        # Place
        self.place(relx=0.0, rely=0.0, relwidth=1, relheight=1, anchor="nw")
