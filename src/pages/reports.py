import customtkinter as ctk

from theme import *

import os
import glob
from datetime import datetime


class ReportsPage(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            fg_color="transparent"
        )

        # ====================================================
        # MAIN LAYOUT
        # ====================================================

        self.grid_columnconfigure(0, weight=4)
        self.grid_columnconfigure(1, weight=2)

        self.grid_rowconfigure(0, weight=1)

        # ====================================================
        # REPORT PREVIEW
        # ====================================================

        preview_card = ctk.CTkFrame(
            self,
            fg_color=CARD,
            corner_radius=18
        )

        preview_card.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(0, 15)
        )

        preview_card.grid_rowconfigure(1, weight=1)
        preview_card.grid_columnconfigure(0, weight=1)

        # ---------------- Header ----------------

        ctk.CTkLabel(
            preview_card,
            text="📄 Report Preview",
            font=("Segoe UI", 18, "bold")
        ).grid(
            row=0,
            column=0,
            sticky="w",
            padx=20,
            pady=(15, 12)
        )

        # ---------------- Textbox ----------------

        self.preview = ctk.CTkTextbox(
            preview_card,
            fg_color="#202938",
            corner_radius=14,
            font=("Consolas", 12),
            wrap="word"
        )

        self.preview.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=15,
            pady=(0, 15)
        )

        # Make report preview read-only
        self.preview.configure(
            state="disabled"
        )

        # ====================================================
        # RIGHT PANEL
        # ====================================================

        side = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        side.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        side.grid_columnconfigure(0, weight=1)
        side.grid_rowconfigure(0, weight=0)
        side.grid_rowconfigure(1, weight=1)

        # ====================================================
        # LATEST REPORT CARD
        # ====================================================

        info = ctk.CTkFrame(
            side,
            fg_color=CARD,
            corner_radius=18
        )

        info.grid(
            row=0,
            column=0,
            sticky="ew",
            pady=(0, 15)
        )

        ctk.CTkLabel(
            info,
            text="📄 Latest Report",
            font=("Segoe UI", 16, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(15, 15)
        )

        self.report_name = ctk.CTkLabel(
            info,
            text="No report found",
            font=("Segoe UI", 13, "bold"),
            justify="left"
        )

        self.report_name.pack(
            anchor="w",
            padx=20,
            pady=(0, 5)
        )

        self.report_date = ctk.CTkLabel(
            info,
            text="",
            text_color="gray",
            font=("Segoe UI", 11)
        )

        self.report_date.pack(
            anchor="w",
            padx=20,
            pady=(0, 15)
        )

        # ====================================================
        # ACTIONS CARD
        # ====================================================

        buttons = ctk.CTkFrame(
            side,
            fg_color=CARD,
            corner_radius=18
        )

        buttons.grid(
            row=1,
            column=0,
            sticky="nsew"
        )

        ctk.CTkLabel(
            buttons,
            text="⚙ Report Actions",
            font=("Segoe UI", 16, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(15, 20)
        )

        # ---------------- Open Report ----------------

        ctk.CTkButton(
            buttons,
            text="📄 Open Report",
            height=42,
            hover_color=BLUE,
            command=self.open_report
        ).pack(
            fill="x",
            padx=20,
            pady=10
        )

        # ---------------- Refresh ----------------

        ctk.CTkButton(
            buttons,
            text="🔄 Refresh",
            height=42,
            hover_color=BLUE,
            command=self.load_latest_report
        ).pack(
            fill="x",
            padx=20,
            pady=10
        )


        # ====================================================
        # LOAD REPORT
        # ====================================================

        self.latest_report = None

        self.load_latest_report()

    # ====================================================
    # LOAD LATEST REPORT
    # ====================================================

    def load_latest_report(self):

        reports = glob.glob("reports/*.txt")

        if not reports:

            self.latest_report = None

            self.preview.configure(
                state="normal"
            )

            self.preview.delete(
                "1.0",
                "end"
            )

            self.preview.insert(
                "end",
                "No reports available."
            )

            self.preview.configure(
                state="disabled"
            )

            self.report_name.configure(
                text="No report found"
            )

            self.report_date.configure(
                text=""
            )

            return

        # Find newest report

        latest = max(
            reports,
            key=os.path.getmtime
        )

        self.latest_report = latest

        # Update report name

        self.report_name.configure(
            text=os.path.basename(latest)
        )

        # Update date

        modified_time = os.path.getmtime(latest)

        date_text = datetime.fromtimestamp(
            modified_time
        ).strftime(
            "%d %b %Y, %H:%M"
        )

        self.report_date.configure(
            text=f"Generated: {date_text}"
        )

        # Read report

        with open(
            latest,
            "r"
        ) as file:

            text = file.read()

        # Update preview

        self.preview.configure(
            state="normal"
        )

        self.preview.delete(
            "1.0",
            "end"
        )

        self.preview.insert(
            "end",
            text
        )

        self.preview.configure(
            state="disabled"
        )

    # ====================================================
    # OPEN REPORT
    # ====================================================

    def open_report(self):

        if self.latest_report:

            os.startfile(
                self.latest_report
            )
