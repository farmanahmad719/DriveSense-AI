import customtkinter as ctk

from src.components.layout.gauge_row import GaugeRow
from src.components.layout.small_metrics_row import SmallMetricsRow
from src.components.cards.graph_card import GraphCard


class RightPanel(ctk.CTkFrame):

    def __init__(self,parent):

        super().__init__(
            parent,
            fg_color="transparent"
        )


        self.grid_rowconfigure(0, weight=0)   # Gauges
        self.grid_rowconfigure(1, weight=0)   # Small metrics
        self.grid_rowconfigure(2, weight=1)   # Graph grows

        self.grid_columnconfigure(0, weight=1)


        GaugeRow(self).grid(
            row=0,
            column=0,
            sticky="ew",
            pady=8
        )


        SmallMetricsRow(self).grid(
            row=1,
            column=0,
            sticky="ew",
            pady=8
        )


        GraphCard(self).grid(
            row=2,
            column=0,
            sticky="nsew",
            pady=8
        )