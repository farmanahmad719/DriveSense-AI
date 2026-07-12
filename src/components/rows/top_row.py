import customtkinter as ctk
from theme import *

from src.components.cards.camera_card import CameraCard
from src.components.cards.gauge_card import GaugeCard


class TopRow(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            fg_color="transparent"
        )

        self.grid_columnconfigure(0, weight=3)

        self.grid_columnconfigure(1, weight=1)

        self.grid_columnconfigure(2, weight=1)

        self.grid_columnconfigure(3, weight=1)

        self.grid_columnconfigure(4, weight=1)

        camera = CameraCard(self)

        camera.grid(row=0,column=0,sticky="nsew",padx=8)

        GaugeCard(
            self,
            "Attention",
            73,
            "#00E676"
            ).grid(row=0,column=1,sticky="nsew",padx=8)

        GaugeCard(
            self,
            "Drowsiness",
            61,
            "#FFA726"
            ).grid(row=0,column=2,sticky="nsew",padx=8)

        GaugeCard(
            self,
            "Blink",
            42,
            "#29B6F6"
            ).grid(row=0,column=3,sticky="nsew",padx=8)

        GaugeCard(
            self,
            "EAR",
            84,
            "#AB47BC"
            ).grid(row=0,column=4,sticky="nsew",padx=8)