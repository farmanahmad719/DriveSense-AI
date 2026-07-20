import customtkinter as ctk

from theme import *
from src.alerts.alert_system import AlertSystem


class AlertCard(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            fg_color=CARD,
            corner_radius=18,
            height=180
        )

        self.pack_propagate(False)

        # ---------------- Title ----------------

        title = ctk.CTkLabel(
            self,
            text="🚨 Alerts",
            font=("Segoe UI", 14, "bold")
        )

        title.pack(
            anchor="w",
            padx=15,
            pady=(15, 10)
        )

        # ---------------- Alert Textbox ----------------

        self.textbox = ctk.CTkTextbox(
            self,
            fg_color="#222B3A",
            font=("Segoe UI Emoji", 12)
        )

        self.textbox.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=(0, 15)
        )

        # ---------------- Alert System ----------------

        self.alert_system = AlertSystem()

        # Prevent repeated alerts every frame
        self.previous_drowsy = False
        self.previous_distracted = False
        self.previous_yawn_count = 0

        # Initial alert
        self.alert_system.add_alert(
            "INFO",
            "Drive session started"
        )

        self.refresh_alerts()

    # =======================================

    def update_data(self, result):

        # ---------------- Drowsiness ----------------

        if result.is_drowsy and not self.previous_drowsy:

            self.add_alert(
                "CRITICAL",
                "Driver Drowsiness Detected"
            )

        self.previous_drowsy = result.is_drowsy

        # ---------------- Distraction ----------------

        if result.is_distracted and not self.previous_distracted:

            self.add_alert(
                "WARNING",
                "Driver Distracted"
            )

        self.previous_distracted = result.is_distracted

        # ---------------- Yawn ----------------

        if result.yawn_count > self.previous_yawn_count:

            self.add_alert(
                "WARNING",
                "Yawn Detected"
            )

        self.previous_yawn_count = result.yawn_count

    # =======================================

    def refresh_alerts(self):

        self.textbox.delete(
            "1.0",
            "end"
        )

        self.textbox.tag_config(
            "INFO",
            foreground=ACCENT
        )

        self.textbox.tag_config(
            "WARNING",
            foreground=ORANGE
        )

        self.textbox.tag_config(
            "CRITICAL",
            foreground=RED
        )

        for alert in self.alert_system.get_alerts():

            severity = alert["severity"]

            self.textbox.insert(
                "end",
                "● ",
                severity
            )

            self.textbox.insert(
                "end",
                f"{alert['time']}   {alert['message']}\n"
            )

        self.textbox.see(
            "end"
        )

    # =======================================

    def add_alert(self, severity, message):

        self.alert_system.add_alert(
            severity,
            message
        )

        self.refresh_alerts()