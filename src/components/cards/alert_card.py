import customtkinter as ctk
import os

from theme import *


class AlertCard(ctk.CTkFrame):

    def __init__(self, parent, alert_system):

        super().__init__(
            parent,
            fg_color=CARD,
            corner_radius=18,
            height=180
        )
        self.alert_system = alert_system

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
        self.view_button = ctk.CTkButton(
            self,
            text="📸 View Latest Screenshot",
            command=self.view_latest_screenshot
        )

        self.view_button.pack(
            pady=(0, 15)
        )

        # ---------------- Alert System ----------------

        self.alert_system = alert_system
        print(
            "AlertCard AlertSystem:",
            id(self.alert_system)
        )

        # Prevent repeated alerts every frame
        self.previous_drowsy = False
        self.previous_distracted = False
        self.previous_yawn_count = 0
        self.previous_phone_detected = False

        self.refresh_alerts()

    # =======================================

    def update_data(self, result):

        # ---------------- Drowsiness ----------------
        if result.is_drowsy and not self.previous_drowsy:

            screenshot = self.find_latest_screenshot(
                "drowsiness"
            )

            self.add_alert(
                "CRITICAL",
                "Driver Drowsiness Detected",
                screenshot
            )

        self.previous_drowsy = result.is_drowsy

        # ---------------- Distraction ----------------

        if result.is_distracted and not self.previous_distracted:

            screenshot = self.find_latest_screenshot(
                "distraction"
            )

            self.add_alert(
                "WARNING",
                "Driver Distracted",
                screenshot
            )

        self.previous_distracted = result.is_distracted

        # ---------------- Yawn ----------------

        if result.yawn_count > self.previous_yawn_count:

            self.add_alert(
                "WARNING",
                "Yawn Detected"
            )

        self.previous_yawn_count = result.yawn_count
        # ---------------- Phone ----------------

        if (
            result.phone_detected
            and not self.previous_phone_detected
        ):

            self.add_alert(
                "CRITICAL",
                "Phone Usage Detected"
            )

        self.previous_phone_detected = (
            result.phone_detected
        )

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

    def add_alert(
            self,
            severity,
            message,
            screenshot=None
        ):

            self.alert_system.add_alert(
                severity,
                message,
                screenshot
            )

            self.refresh_alerts()
    def find_latest_screenshot(self, event):

        if not os.path.exists("alerts"):

            return None

        files = [

            file

            for file in os.listdir("alerts")

            if file.startswith(event)

            and file.endswith(".png")
        ]

        if not files:

            return None

        files.sort(
            key=lambda file: os.path.getmtime(
                os.path.join(
                    "alerts",
                    file
                )
            ),
            reverse=True
        )

        return os.path.join(
            "alerts",
            files[0]
        )    
    def view_latest_screenshot(self):

        if not os.path.exists("alerts"):

            return

        files = [

            file

            for file in os.listdir("alerts")

            if file.endswith(".png")
        ]

        if not files:

            return

        files.sort(
            key=lambda file: os.path.getmtime(
                os.path.join(
                    "alerts",
                    file
                )
            ),
            reverse=True
        )

        latest_file = os.path.join(
            "alerts",
            files[0]
        )

        os.startfile(
            latest_file
        )    