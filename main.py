import customtkinter as ctk
from dotenv import load_dotenv

from ui.root import Root

def main():
    load_dotenv()

    app = Root()
    app.mainloop()

if __name__ == "__main__":
    main()