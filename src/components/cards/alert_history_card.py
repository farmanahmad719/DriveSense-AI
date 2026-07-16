import customtkinter as ctk
from theme import *

from src.alerts.alert_system import AlertSystem


class AlertHistoryCard(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            fg_color=CARD,
            corner_radius=18
        )

        self.alert_system = AlertSystem()

        # ================= Header =================

        header = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        header.pack(
            fill="x",
            padx=20,
            pady=(15,15)
        )

        ctk.CTkLabel(
            header,
            text="🚨 Alert History",
            font=("Segoe UI",18,"bold")
        ).pack(side="left")

        self.total = ctk.CTkLabel(
            header,
            text="Total Alerts: 0",
            text_color="#00E676",
            font=("Segoe UI",13,"bold")
        )

        self.total.pack(side="right")

        # ================= Textbox =================

        self.textbox = ctk.CTkTextbox(
            self,
            fg_color="#252F40",
            corner_radius=12,
            font=("Consolas",14)
        )

        self.textbox.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0,20)
        )

        # Sample alerts

        self.alert_system.add_alert("INFO","Drive session started")
        self.alert_system.add_alert("INFO","Driver Awake")
        self.alert_system.add_alert("WARNING","Yawn Detected")
        self.alert_system.add_alert("CRITICAL","Driver Distracted")

        self.refresh_alerts()

    # ===================================================

    def refresh_alerts(self):

        self.textbox.configure(state="normal")

        self.textbox.delete("1.0","end")

        self.textbox.tag_config(
            "info",
            foreground="#00E676"
        )

        self.textbox.tag_config(
            "warning",
            foreground="#FFB000"
        )

        self.textbox.tag_config(
            "critical",
            foreground="#FF4C4C"
        )

        alerts = self.alert_system.get_alerts()

        self.total.configure(
            text=f"Total Alerts: {len(alerts)}"
        )

        dots = {
            "INFO":"●",
            "WARNING":"●",
            "CRITICAL":"●"
        }

        for alert in alerts:

            severity = alert["severity"]

            tag = severity.lower()

            self.textbox.insert(
                "end",
                dots[severity] + " ",
                tag
            )

            self.textbox.insert(
                "end",
                f"{alert['time']}    {alert['message']}\n\n"
            )

    
        self.textbox.see("1.0")
        self.textbox.configure(state="disabled")