import customtkinter as ctk
from theme import *
import os
import glob
import subprocess


class Sidebar(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            width=240,
            fg_color=SIDEBAR,
            corner_radius=0
        )

        self.grid_propagate(False)

        # ---------------- Logo ----------------

        self.logo = ctk.CTkLabel(
            self,
            text="🚗 DriveSense AI",
            font=("Segoe UI", 22, "bold"),
            text_color="white"
        )

        self.logo.pack(pady=(30, 40))

        # ---------------- Navigation ----------------
        
        self.menu_buttons = {}

        menus = [
            "Dashboard",
            "Live Monitoring",
            "Analytics",
            "Alerts",
            "Reports",
            "Settings",
            "Help"
        ]

        for item in menus:

            button = ctk.CTkButton(
                self,
                text=item,
                fg_color="transparent",
                hover_color="#12354F",
                anchor="w",
                height=45,
                font=("Segoe UI", 15),
                command=lambda i=item: self.select_menu(i)
            )

            button.pack(
                fill="x",
                padx=15,
                pady=5
            )

            self.menu_buttons[item] = button

        # ---------------- Push utilities to bottom ----------------

        ctk.CTkLabel(
            self,
            text=""
        ).pack(expand=True)

        # ---------------- Divider ----------------

        divider = ctk.CTkFrame(
            self,
            height=2,
            fg_color=BORDER
        )

        divider.pack(
            fill="x",
            padx=20,
            pady=(10, 15)
        )

        # ---------------- Generate Report ----------------

        report_btn = ctk.CTkButton(
            self,
            text="📄 Generate Report",
            height=42,
            corner_radius=12,
            fg_color="#1B2433",
            hover_color=BLUE,
            font=("Segoe UI", 14, "bold"),
            command=self.open_latest_report
        )

        report_btn.pack(
            fill="x",
            padx=15,
            pady=5
        )

        # ---------------- Test Alarm ----------------

        alarm_btn = ctk.CTkButton(
            self,
            text="🔔 Test Alarm",
            height=42,
            corner_radius=12,
            fg_color="#1B2433",
            hover_color=BLUE,
            font=("Segoe UI", 14, "bold")
        )

        alarm_btn.pack(
            fill="x",
            padx=15,
            pady=(5, 20)
        )
        self.select_menu("Dashboard")

        self.select_menu("Dashboard")

    def open_latest_report(self):

        reports = glob.glob("reports/*.txt")

        if not reports:
            print("No reports found.")
            return

        latest_report = max(reports, key=os.path.getmtime)

        os.startfile(latest_report)

    def select_menu(self, selected):

        for name, button in self.menu_buttons.items():

            if name == selected:

                button.configure(
                        fg_color="#165C3D"   # translucent green
                )

            else:

                button.configure(
                    fg_color="transparent"
                )