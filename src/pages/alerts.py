import customtkinter as ctk

from theme import *

from src.components.cards.alert_card import AlertCard


class AlertsPage(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            fg_color="transparent"
        )

        # ================= Layout =================

        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=1)

        self.grid_rowconfigure(0, weight=1)

        # ====================================================
        # Alert History
        # ====================================================

        history = AlertCard(self)

        history.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(0,15)
        )

        # ====================================================
        # Right Panel
        # ====================================================

        right = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        right.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        right.grid_rowconfigure(0, weight=0)
        right.grid_rowconfigure(1, weight=1)

        # ====================================================
        # Summary
        # ====================================================

        summary = ctk.CTkFrame(
            right,
            fg_color=CARD,
            corner_radius=18
        )

        summary.grid(
            row=0,
            column=0,
            sticky="ew",
            pady=(0,15)
        )

        ctk.CTkLabel(
            summary,
            text="📊 Alert Summary",
            font=("Segoe UI",16,"bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(15,15)
        )

        stats = [
            ("INFO", "15"),
            ("WARNING", "8"),
            ("CRITICAL", "2")
        ]

        for label, value in stats:

            row = ctk.CTkFrame(
                summary,
                fg_color="transparent"
            )

            row.pack(
                fill="x",
                padx=20,
                pady=6
            )

            ctk.CTkLabel(
                row,
                text=label,
                font=("Segoe UI",13)
            ).pack(side="left")

            ctk.CTkLabel(
                row,
                text=value,
                font=("Segoe UI",13,"bold")
            ).pack(side="right")

        # ====================================================
        # Actions
        # ====================================================

        actions = ctk.CTkFrame(
            right,
            fg_color=CARD,
            corner_radius=18
        )

        actions.grid(
            row=1,
            column=0,
            sticky="nsew"
        )

        ctk.CTkLabel(
            actions,
            text="⚙ Actions",
            font=("Segoe UI",16,"bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(15,20)
        )

        ctk.CTkButton(
            actions,
            text="🗑 Clear Alerts",
            height=42,
            hover_color=BLUE
        ).pack(
            fill="x",
            padx=20,
            pady=10
        )

        ctk.CTkButton(
            actions,
            text="💾 Export Logs",
            height=42,
            hover_color=BLUE
        ).pack(
            fill="x",
            padx=20,
            pady=10
        )