import customtkinter as ctk
from theme import *


class DriverCard(ctk.CTkFrame):

    def __init__(self,parent):

        super().__init__(
            parent,
            fg_color=CARD,
            corner_radius=18,
            height=220
        )

        self.grid_propagate(False)

        ctk.CTkLabel(
            self,
            text="👤 Driver",
            font=("Segoe UI",18,"bold")
        ).pack(pady=(15,20))

        ctk.CTkLabel(
            self,
            text="AWAKE",
            text_color="#00E676",
            font=("Segoe UI",28,"bold")
        ).pack()