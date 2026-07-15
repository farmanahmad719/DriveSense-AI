import customtkinter as ctk

from src.components.cards.graph_card import GraphCard


class GraphRow(ctk.CTkFrame):

    def __init__(self,parent):

        super().__init__(
            parent,
            fg_color="transparent"
        )

        self.grid_columnconfigure(0,weight=1)

        graph = GraphCard(self)

        graph.grid(
            row=0,
            column=0,
            sticky="nsew"
        )