import customtkinter as ctk
from theme import *


class Navbar(ctk.CTkFrame):

    def __init__(self,parent):

        super().__init__(

            parent,

            height=70,

            fg_color=CARD,

            corner_radius=15

        )

        self.grid_propagate(False)

        title = ctk.CTkLabel(

            self,

            text="Dashboard",

            font=("Segoe UI",24,"bold")

        )

        title.pack(
            side="left",
            padx=25
        )

        user = ctk.CTkLabel(

            self,

            text="Hello, Farman",

            font=("Segoe UI",16)

        )

        user.pack(
            side="right",
            padx=25
        )