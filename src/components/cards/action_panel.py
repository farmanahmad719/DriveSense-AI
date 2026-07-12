import customtkinter as ctk
from theme import *


class ActionPanel(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            fg_color="transparent",
            width=220
        )

        self.grid_propagate(False)

        self.selected = "Attention"

        self.metric_buttons = {}

        # ---------- GRID ----------

        self.grid_columnconfigure((0, 1), weight=1, uniform="buttons")
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        title = ctk.CTkLabel(
            self,
            text="Live Analytics",
            font=("Segoe UI", 18, "bold")
        )

        title.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="w",
            pady=(5, 15)
        )

        metrics = [
            ("Attention", 1, 0),
            ("Blink Rate", 1, 1),
            ("Drowsiness", 2, 0),
            ("EAR", 2, 1)
        ]

        for metric, row, column in metrics:

            color = ORANGE if metric == self.selected else BORDER

            btn = ctk.CTkButton(
                self,
                text=metric,
                height=60,
                corner_radius=15,
                fg_color=color,
                hover_color=TEXT_SECONDARY,
                font=("Segoe UI", 14, "bold")
            )

            btn.grid(
                row=row,
                column=column,
                padx=6,
                pady=6,
                sticky="nsew"
            )

            self.metric_buttons[metric] = btn