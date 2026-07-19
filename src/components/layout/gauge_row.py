import customtkinter as ctk

from src.components.cards.gauge_card import GaugeCard


class GaugeRow(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            fg_color="transparent"
        )

        for i in range(4):

            self.grid_columnconfigure(
                i,
                weight=1
            )

        self.attention_gauge = GaugeCard(
            self,
            "Attention",
            85,
            "#00E676"
        )

        self.attention_gauge.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=8
        )

        self.drowsiness_gauge = GaugeCard(
            self,
            "Drowsiness",
            20,
            "#FFA726"
        )

        self.drowsiness_gauge.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=8
        )

        self.blink_gauge = GaugeCard(
            self,
            "Blink Rate",
            60,
            "#29B6F6"
        )

        self.blink_gauge.grid(
            row=0,
            column=2,
            sticky="nsew",
            padx=8
        )

        self.ear_gauge = GaugeCard(
            self,
            "EAR",
            75,
            "#AB47BC"
        )

        self.ear_gauge.grid(
            row=0,
            column=3,
            sticky="nsew",
            padx=8
        )
    def update_value(self, value):

        self.gauge.set_value(value)    