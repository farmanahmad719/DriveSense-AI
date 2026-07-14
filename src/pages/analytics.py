import customtkinter as ctk

from src.components.charts.attention_graph import AttentionGraph


class AnalyticsPage(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            fg_color="transparent"
        )

        # ================= Grid =================

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # ================= Attention =================

        self.attention = AttentionGraph(self)
        self.attention.grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        self.attention.show_metric("Attention")

        # ================= Blink =================

        self.blink = AttentionGraph(self)
        self.blink.grid(
            row=0,
            column=1,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        self.blink.show_metric("Blink Rate")

        # ================= Drowsiness =================

        self.drowsiness = AttentionGraph(self)
        self.drowsiness.grid(
            row=1,
            column=0,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        self.drowsiness.show_metric("Drowsiness")

        # ================= EAR =================

        self.ear = AttentionGraph(self)
        self.ear.grid(
            row=1,
            column=1,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        self.ear.show_metric("EAR")