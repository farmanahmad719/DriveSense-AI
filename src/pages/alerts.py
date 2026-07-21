import customtkinter as ctk

from theme import *

from src.components.cards.alert_card import AlertCard
import csv

from tkinter import filedialog


class AlertsPage(ctk.CTkFrame):

    def __init__(self, parent,alert_system):

        super().__init__(
            parent,
            fg_color="transparent"
        )
        self.alert_system = alert_system
        print(
            "AlertsPage AlertSystem:",
            id(self.alert_system)
        )
                # ================= Layout =================

        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=1)

        self.grid_rowconfigure(0, weight=1)

        # ====================================================
        # Alert History
        # ====================================================

        self.history = AlertCard(
            self,
            self.alert_system
        )
        self.history.grid(
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

        self.summary_labels = {}

        stats = [
            "INFO",
            "WARNING",
            "CRITICAL"
        ]

        for severity in stats:

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
                text=severity,
                font=("Segoe UI", 13)
            ).pack(
                side="left"
            )

            value_label = ctk.CTkLabel(
                row,
                text="0",
                font=("Segoe UI", 13, "bold")
            )

            value_label.pack(
                side="right"
            )

            self.summary_labels[severity] = value_label

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
        # Clear button
        ctk.CTkButton(
            actions,
            text="🗑 Clear Alerts",
            height=42,
            hover_color=BLUE,
            command=self.clear_alerts
        ).pack(
            fill="x",
            padx=20,
            pady=10
        )

        # Export button
        ctk.CTkButton(
            actions,
            text="💾 Export Logs",
            height=42,
            hover_color=BLUE,
            command=self.export_logs
        ).pack(
            fill="x",
            padx=20,
            pady=10
        )
        self.refresh_page()
    def refresh_page(self):

        self.history.refresh_alerts()

        self.update_summary()

        self.after(
            500,
            self.refresh_page
        )
    def update_detection_result(self, result):

        self.history.update_data(
            result
        )    
    def update_summary(self):

        alerts = self.alert_system.get_alerts()

        counts = {
            "INFO": 0,
            "WARNING": 0,
            "CRITICAL": 0
        }

        for alert in alerts:

            severity = alert["severity"]

            if severity in counts:

                counts[severity] += 1

        for severity in counts:

            self.summary_labels[severity].configure(
                text=str(
                    counts[severity]
                )
            )    
    def clear_alerts(self):

        self.alert_system.clear()

        self.history.refresh_alerts()

        self.update_summary()      
    def export_logs(self):

        alerts = self.alert_system.get_alerts()

        if not alerts:

            print(
                "No alerts to export."
            )

            return

        file_path = filedialog.asksaveasfilename(

            title="Export Alert Logs",

            defaultextension=".csv",

            filetypes=[
                (
                    "CSV Files",
                    "*.csv"
                ),
                (
                    "All Files",
                    "*.*"
                )
            ]
        )

        if not file_path:

            return

        with open(
            file_path,
            "w",
            newline=""
        ) as file:

            writer = csv.DictWriter(

                file,

                fieldnames=[
                    "time",
                    "severity",
                    "message",
                    "screenshot"
                ]
            )

            writer.writeheader()

            writer.writerows(
                alerts
            )

        print(
            f"Alert logs exported to:\n{file_path}"
        )