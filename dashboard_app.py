import customtkinter as ctk

from src.pages.dashboard import Dashboard

# Global Theme
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


def main():
    app = Dashboard()
    app.mainloop()


if __name__ == "__main__":
    main()