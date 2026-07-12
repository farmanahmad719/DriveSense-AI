import customtkinter as ctk
from theme import *


class TripCard(ctk.CTkFrame):

    def __init__(self,parent):

        super().__init__(
            parent,
            fg_color=CARD,
            corner_radius=18,
            height=180
        )

        self.grid_propagate(False)

        ctk.CTkLabel(
            self,
            text="📊 Trip Summary",
            font=("Segoe UI",18,"bold")
        ).pack(pady=15)

        stats = [
            ("Duration","00:13"),
            ("Alerts","03"),
            ("Attention","86%"),
            ("Risk","Low")
        ]

        for key,value in stats:

            row = ctk.CTkFrame(
                self,
                fg_color="transparent"
            )

            row.pack(fill="x",padx=15,pady=4)

            ctk.CTkLabel(
                row,
                text=key
            ).pack(side="left")

            ctk.CTkLabel(
                row,
                text=value,
                font=("Segoe UI",13,"bold")
            ).pack(side="right")