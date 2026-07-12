import customtkinter as ctk
from theme import *

class SmallCard(ctk.CTkFrame):

    def __init__(self, parent, title, value, color):

        super().__init__(
            parent,
            fg_color=CARD,
            corner_radius=15,
            width=170,
            height=110
        )

        self.grid_propagate(False)

        # Configure rows
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.grid_columnconfigure(0, weight=1)

        title_label = ctk.CTkLabel(
            self,
            text=title,
            font=("Segoe UI", 14)
        )

        title_label.grid(
            row=0,
            column=0,
            sticky="s"
        )

        value_label = ctk.CTkLabel(
            self,
            text=value,
            text_color=color,
            font=("Segoe UI", 22, "bold")
        )

        value_label.grid(
            row=1,
            column=0,
            sticky="n",
            pady=(2,15)
        )