import customtkinter as ctk
from theme import *

from src.components.charts.attention_graph import AttentionGraph


class GraphCard(ctk.CTkFrame):

    def __init__(self,parent):

        super().__init__(
            parent,
            fg_color=CARD,
            corner_radius=20,
        )

        title = ctk.CTkLabel(
            self,
            text="Attention Trend",
            font=("Segoe UI",18,"bold")
        )

        title.pack(
            anchor="w",
            padx=20,
            pady=(15,5)
        )

        graph = AttentionGraph(self)

        graph.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=(5,15)
        )