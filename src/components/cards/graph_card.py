import customtkinter as ctk
from theme import *

from src.components.charts.attention_graph import AttentionGraph
from src.components.cards.action_panel import ActionPanel


class GraphCard(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            fg_color=CARD,
            corner_radius=20
        )

        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=2)

        self.grid_rowconfigure(0, weight=1)


        graph = AttentionGraph(self)

        graph.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(15, 5),
            pady=15
        )

        panel = ActionPanel(self)

        panel.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=(5, 15),
            pady=15
        )