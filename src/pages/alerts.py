import customtkinter as ctk

from theme import *

from src.components.cards.alert_history_card import AlertHistoryCard
from src.components.cards.system_status_card import SystemStatusCard

class AlertsPage(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            fg_color="transparent"
        )

        # ================= Layout =================

        self.grid_columnconfigure(0, weight=5)
        self.grid_columnconfigure(1, weight=2)

        self.grid_rowconfigure(0, weight=1)

        # ====================================================
        # Alert History
        # ====================================================

        self.history = AlertHistoryCard(self)

        self.history.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(0,15)
        )

        alerts = self.history.alert_system.get_alerts()

        info = sum(a["severity"] == "INFO" for a in alerts)
        warning = sum(a["severity"] == "WARNING" for a in alerts)
        critical = sum(a["severity"] == "CRITICAL" for a in alerts)

        latest = alerts[0] if alerts else None

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

        right.grid_rowconfigure(0, weight=2)
        right.grid_rowconfigure(1, weight=1)
        right.grid_rowconfigure(2, weight=1)

        right.grid_columnconfigure(0, weight=1)


        # ====================================================
        # Summary
        # ====================================================

        summary = ctk.CTkFrame(
            right,
            fg_color=CARD,
            corner_radius=18,
            height=390
        )

        summary.grid_propagate(False)

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

        # ====================================================
        # Statistics
        # ====================================================

        stats = [
            ("INFO", info, "#00E676"),
            ("WARNING", warning, "#FFB000"),
            ("CRITICAL", critical, "#FF4C4C")
        ]

        for i, (label, value, color) in enumerate(stats):

            row = ctk.CTkFrame(
                summary,
                fg_color="transparent"
            )

            row.pack(
                fill="x",
                padx=20,
                pady=5
            )

            left = ctk.CTkFrame(
                row,
                fg_color="transparent"
            )

            left.pack(side="left")

            ctk.CTkLabel(
                left,
                text="■",
                text_color=color,
                font=("Segoe UI",18,"bold")
            ).pack(side="left")

            ctk.CTkLabel(
                left,
                text=f"  {label}",
                font=("Segoe UI",13)
            ).pack(side="left")

            ctk.CTkLabel(
                row,
                text=str(value),
                text_color=color,
                font=("Segoe UI",13,"bold")
            ).pack(side="right")

            if i != len(stats)-1:

                ctk.CTkFrame(
                    summary,
                    height=1,
                    fg_color="#263245"
                ).pack(
                    fill="x",
                    padx=20,
                    pady=6
                )

# ====================================================
# Divider
# ====================================================

        ctk.CTkFrame(
            summary,
            height=2,
            fg_color="#313C4E"
        ).pack(
            fill="x",
            padx=20,
            pady=15
        )

# ====================================================
# Latest Alert
# ====================================================

        ctk.CTkLabel(
            summary,
            text="Latest Alert",
            font=("Segoe UI",14,"bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(0,10)
        )

        latest_card = ctk.CTkFrame(
            summary,
            fg_color="#252F40",
            corner_radius=12
        )

        latest_card.pack(
            fill="x",
            padx=20,
            pady=(0,15)
        )

        severity_colors = {
            "INFO":"#00E676",
            "WARNING":"#FFB000",
            "CRITICAL":"#FF4C4C"
        }

        if latest:

            severity = latest["severity"]

            top = ctk.CTkFrame(
                latest_card,
                fg_color="transparent"
            )

            top.pack(
                fill="x",
                padx=15,
                pady=(12,6)
            )

            left = ctk.CTkFrame(
                top,
                fg_color="transparent"
            )

            left.pack(side="left")

            ctk.CTkLabel(
                left,
                text="●",
                text_color=severity_colors[severity],
                font=("Segoe UI",18,"bold")
            ).pack(side="left")

            ctk.CTkLabel(
                left,
                text="  " + latest["message"],
                font=("Segoe UI",13,"bold")
            ).pack(side="left")

            bottom = ctk.CTkFrame(
                latest_card,
                fg_color="transparent"
            )

            bottom.pack(
                fill="x",
                padx=15,
                pady=(0,12)
            )

            ctk.CTkLabel(
                bottom,
                text=latest["time"],
                text_color="gray",
                font=("Segoe UI",11)
            ).pack(side="left")

            ctk.CTkLabel(
                bottom,
                text=severity,
                text_color=severity_colors[severity],
                font=("Segoe UI",11,"bold")
            ).pack(side="right")

        # ====================================================
        # Actions
        # ====================================================

        actions = ctk.CTkFrame(
            right,
            fg_color=CARD,
            corner_radius=18,
            height=300
        )

        actions.grid_propagate(False)

        actions.grid(
            row=1,
            column=0,
            sticky="ew",
            pady=(15,15)
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

        # status_card = SystemStatusCard(right)

        # status_card.grid(
        #     row=2,
        #     column=0,
        #     sticky="nsew",
        #     pady=(15,0)
        # )

        