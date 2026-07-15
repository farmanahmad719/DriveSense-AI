import customtkinter as ctk

from src.components.cards.gauge_card import GaugeCard


class GaugeRow(ctk.CTkFrame):

    def __init__(self,parent):

        super().__init__(
            parent,
            fg_color="transparent"
        )


        for i in range(4):
            self.grid_columnconfigure(
                i,
                weight=1
            )


        gauges = [
            ("Attention",85,"#00E676"),
            ("Drowsiness",20,"#FFA726"),
            ("Blink Rate",60,"#29B6F6"),
            ("EAR",75,"#AB47BC")
        ]


        for i,data in enumerate(gauges):

            GaugeCard(
                self,
                data[0],
                data[1],
                data[2]
            ).grid(
                row=0,
                column=i,
                sticky="nsew",
                padx=8
            )