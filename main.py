from customtkinter import set_widget_scaling, set_window_scaling
from dotenv import load_dotenv

from ui.root import Root


def main():
    # Load .env for env variables
    load_dotenv()

    # Create root widget
    app = Root()

    app.title("Misc")

    scale_factor = app.tk.call("tk", "scaling")
    set_window_scaling(scale_factor)
    set_widget_scaling(scale_factor)

    app.async_mainloop()


if __name__ == "__main__":
    main()
