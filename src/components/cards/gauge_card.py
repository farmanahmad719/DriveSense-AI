import customtkinter as ctk
from theme import *

from src.components.widgets.circular_gauge import CircularGauge


class GaugeCard(ctk.CTkFrame):

    def __init__(self, parent, title, value, color):

        super().__init__(
            parent,
            fg_color=CARD,
            corner_radius=20,
            width=190,
            height=260
        )

        self.grid_propagate(False)

        self.grid_rowconfigure((0,1,2), weight=1)
        self.grid_columnconfigure(0, weight=1)

        title_label = ctk.CTkLabel(
            self,
            text=title,
            font=("Segoe UI",16,"bold")
        )

        title_label.grid(
            row=0,
            column=0,
            pady=(15,5)
        )

        self.gauge = CircularGauge(
            self,
            size=120,
            color=color
        )

        self.gauge.grid(
            row=1,
            column=0
        )

        self.gauge.set_value(value)

        self.live = ctk.CTkLabel(
            self,
            text="● LIVE",
            text_color="#00E676",
            font=("Segoe UI",11)
        )

        self.live.grid(
            row=2,
            column=0,
            pady=(0,15)
        )