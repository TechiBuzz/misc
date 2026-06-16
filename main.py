from dotenv import load_dotenv
from ui.root import Root

def main():
    # Load .env for env variables
    load_dotenv()

    # Create root widget
    app = Root()
    app.async_mainloop()

if __name__ == "__main__":
    main()