import customtkinter as ctk
from theme import *

import os
import glob


class ReportsPage(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            fg_color="transparent"
        )

        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=1)

        self.grid_rowconfigure(0, weight=1)

        # ==========================================
        # Report Preview
        # ==========================================

        self.preview = ctk.CTkTextbox(
            self,
            fg_color=CARD,
            corner_radius=18,
            font=("Consolas", 12)
        )

        self.preview.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(0,15)
        )

        # ==========================================
        # Right Panel
        # ==========================================

        side = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        side.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        # ==========================================
        # Report Info
        # ==========================================

        info = ctk.CTkFrame(
            side,
            fg_color=CARD,
            corner_radius=18
        )

        info.pack(
            fill="x",
            pady=(0,15)
        )

        ctk.CTkLabel(
            info,
            text="📄 Latest Report",
            font=("Segoe UI",16,"bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(15,15)
        )

        self.report_name = ctk.CTkLabel(
            info,
            text="No report found",
            justify="left"
        )

        self.report_name.pack(
            anchor="w",
            padx=20,
            pady=(0,15)
        )

        # ==========================================
        # Buttons
        # ==========================================

        buttons = ctk.CTkFrame(
            side,
            fg_color=CARD,
            corner_radius=18
        )

        buttons.pack(
            fill="both",
            expand=True
        )

        ctk.CTkLabel(
            buttons,
            text="⚙ Report Actions",
            font=("Segoe UI",16,"bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(15,20)
        )

        ctk.CTkButton(
            buttons,
            text="📄 Open Report",
            hover_color=BLUE,
            command=self.load_latest_report
        ).pack(
            fill="x",
            padx=20,
            pady=10
        )

        ctk.CTkButton(
            buttons,
            text="🔄 Refresh",
            hover_color=BLUE,
            command=self.load_latest_report
        ).pack(
            fill="x",
            padx=20,
            pady=10
        )

        self.load_latest_report()

    def load_latest_report(self):

        reports = glob.glob("reports/*.txt")

        if not reports:

            self.preview.delete("1.0", "end")
            self.preview.insert("end", "No reports available.")
            return

        latest = max(
            reports,
            key=os.path.getmtime
        )

        self.report_name.configure(
            text=os.path.basename(latest)
        )

        with open(latest, "r") as file:

            text = file.read()

        self.preview.delete("1.0", "end")
        self.preview.insert("end", text)