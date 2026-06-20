from customtkinter import CTkFrame, CTkLabel, CTkProgressBar

from util.constants import Fonts


class LoadingPage(CTkFrame):
    def __init__(self, parent, transition_time_ms: int):
        super().__init__(parent)

        # Widgets
        self.central_frame = CTkFrame(self, corner_radius=15)

        self.central_frame.columnconfigure(0, weight=1)
        self.central_frame.rowconfigure((0, 1), weight=1, uniform="RE")

        self.central_frame.place(
            relx=0.5, rely=0.5, relheight=0.93, relwidth=0.95, anchor="center"
        )

        self.text = CTkLabel(self.central_frame, text="Loading...", font=Fonts.LOADING)
        self.text.grid(column=0, row=0, sticky="s", pady=30)

        self.progress_bar = CTkProgressBar(
            self.central_frame,
            width=700,
            height=10,
            mode="indeterminate",
        )
        self.progress_bar.grid(column=0, row=1, sticky="n", pady=80)

        # Place
        self.place(relx=0.0, rely=0.0, relwidth=1, relheight=1, anchor="nw")

        self.after(int(transition_time_ms * 0.70), self.change_text)

        # Start progress
        self.progress_bar.start()

    def change_text(self):
        self.text.configure(text="Complete!")
        self.progress_bar.stop()
