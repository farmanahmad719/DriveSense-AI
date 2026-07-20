import customtkinter as ctk
from theme import *
from datetime import datetime


class TripCard(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            fg_color=CARD,
            corner_radius=18,
            height=180
        )

        self.pack_propagate(False)

        # ---------------- Title ----------------

        ctk.CTkLabel(
            self,
            text="📊 Trip Summary",
            font=("Segoe UI", 14, "bold")
        ).pack(
            pady=9
        )

        # ---------------- Values ----------------

        self.value_labels = {}

        self.add_row(
            "Duration",
            "00:00"
        )

        self.add_row(
            "Alerts",
            "0"
        )

        self.add_row(
            "Attention",
            "100%"
        )

        self.add_row(
            "Risk",
            "Low"
        )

        # ---------------- Internal State ----------------

        self.start_time = datetime.now()

        self.alert_count = 0

    # =======================================

    def add_row(self, key, value):

        row = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        row.pack(
            fill="x",
            padx=13,
            pady=3
        )

        ctk.CTkLabel(
            row,
            text=key
        ).pack(
            side="left"
        )

        value_label = ctk.CTkLabel(
            row,
            text=value,
            font=("Segoe UI", 13, "bold")
        )

        value_label.pack(
            side="right"
        )

        self.value_labels[key] = value_label

    # =======================================

    def update_data(self, result):

        # ---------------- Attention ----------------

        attention = max(
            0,
            min(
                100,
                100 - result.fatigue_score
            )
        )

        self.value_labels["Attention"].configure(
            text=f"{attention}%"
        )

        # ---------------- Risk ----------------

        if result.is_drowsy:

            risk = "High"

        elif result.is_distracted:

            risk = "Medium"

        elif result.fatigue_score >= 40:

            risk = "Medium"

        else:

            risk = "Low"

        self.value_labels["Risk"].configure(
            text=risk
        )
    def update_alert_count(self, count):

        self.value_labels["Alerts"].configure(
            text=str(count)
        )    
         # =======================================

    def update_duration(self):

        elapsed = datetime.now() - self.start_time

        total_seconds = int(
            elapsed.total_seconds()
        )

        minutes = total_seconds // 60

        seconds = total_seconds % 60

        duration = f"{minutes:02d}:{seconds:02d}"

        self.value_labels["Duration"].configure(
            text=duration
        )   