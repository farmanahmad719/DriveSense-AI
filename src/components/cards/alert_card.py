import customtkinter as ctk
from theme import *

from src.alerts.alert_system import AlertSystem


class AlertCard(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            fg_color=CARD,
            corner_radius=18,
            height=10
        )

        self.pack_propagate(False)

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

        self.alert_system = AlertSystem()

        # Initial Alerts
        self.alert_system.add_alert(
            "INFO",
            "Drive session started"
        )

        self.alert_system.add_alert(
            "INFO",
            "Driver Awake"
        )

        self.refresh_alerts()

        self.add_alert("WARNING", "Yawn Detected")
        self.add_alert("CRITICAL", "Driver Distracted")

    def refresh_alerts(self):
        self.textbox.delete("1.0", "end")

        self.textbox.tag_config("INFO", foreground=ACCENT)
        self.textbox.tag_config("WARNING", foreground=ORANGE)
        self.textbox.tag_config("CRITICAL", foreground=RED)

        for alert in self.alert_system.get_alerts():

            severity = alert["severity"]

        # Colored status dot
            self.textbox.insert("end", "● ", severity)

        # Normal white text
            self.textbox.insert(
                "end",
                f"{alert['time']}   {alert['message']}\n"
            )
        self.textbox.see("end")

    def add_alert(self, severity, message):

        self.alert_system.add_alert(
            severity,
            message
        )

        self.refresh_alerts()