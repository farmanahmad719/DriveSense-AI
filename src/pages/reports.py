import customtkinter as ctk
<<<<<<< HEAD

=======
from datetime import datetime
>>>>>>> 151acb891a5b5ca9cf0a51ae8c9855e06d790cdd
from theme import *
import os
<<<<<<< HEAD
import glob
from datetime import datetime

=======
from src.reports.report_generator import ReportGenerator
>>>>>>> 151acb891a5b5ca9cf0a51ae8c9855e06d790cdd

class ReportsPage(ctk.CTkFrame):

    def __init__(self, parent, dashboard):

        super().__init__(
            parent,
            fg_color="transparent"
        )

<<<<<<< HEAD
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
=======
        self.dashboard = dashboard
        self.report_generator = ReportGenerator()

        self.grid_columnconfigure(
            0,
            weight=1
        )

        self.grid_rowconfigure(
            1,
            weight=1
        )

        # ================= TITLE =================

        ctk.CTkLabel(
            self,
            text="📄 Session Report",
            font=("Segoe UI", 26, "bold")
        ).grid(
            row=0,
            column=0,
            sticky="w",
            padx=20,
            pady=(10, 20)
        )

        # ================= REPORT CARD =================
>>>>>>> 151acb891a5b5ca9cf0a51ae8c9855e06d790cdd

        self.report_card = ctk.CTkFrame(
            self,
            fg_color=CARD,
            corner_radius=20
        )

        self.report_card.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=20,
            pady=(0, 20)
        )

        self.report_card.grid_columnconfigure(
            0,
            weight=1
        )

        self.report_card.grid_columnconfigure(
            1,
            weight=1
        )

        self.metric_labels = {}

        self.create_metric(
            "Total Blinks",
            "0",
            0,
            0
        )

        self.create_metric(
            "Total Yawns",
            "0",
            0,
            1
        )

        self.create_metric(
            "Average Fatigue",
            "0%",
            1,
            0
        )

        self.create_metric(
            "Drowsiness Events",
            "0",
            1,
            1
        )

        self.create_metric(
            "Distraction Events",
            "0",
            2,
            0
        )

        self.create_metric(
            "Average EAR",
            "0.00",
            2,
            1
        )

        self.create_metric(
            "Average MAR",
            "0.00",
            3,
            0
        )

        self.create_metric(
            "Risk Level",
            "LOW",
            3,
            1
        )

        # ================= BUTTON =================

        # ================= BUTTONS =================

        button_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

<<<<<<< HEAD
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
=======
        button_frame.grid(
            row=2,
            column=0,
            pady=(0, 20)
>>>>>>> 151acb891a5b5ca9cf0a51ae8c9855e06d790cdd
        )

        # ---------------- Open Report ----------------

        ctk.CTkButton(
<<<<<<< HEAD
            buttons,
            text="📄 Open Report",
            height=42,
            hover_color=BLUE,
            command=self.open_report
=======
            button_frame,
            text="🔄 Refresh Report",
            command=self.update_report
>>>>>>> 151acb891a5b5ca9cf0a51ae8c9855e06d790cdd
        ).pack(
            side="left",
            padx=10
        )

        # ---------------- Refresh ----------------

        ctk.CTkButton(
<<<<<<< HEAD
            buttons,
            text="🔄 Refresh",
            height=42,
            hover_color=BLUE,
            command=self.load_latest_report
=======
            button_frame,
            text="📄 Generate Report",
            command=self.generate_report
>>>>>>> 151acb891a5b5ca9cf0a51ae8c9855e06d790cdd
        ).pack(
            side="left",
            padx=10
        )
        self.auto_update()

    # =================================================

    def create_metric(
        self,
        name,
        value,
        row,
        column
    ):

        card = ctk.CTkFrame(
            self.report_card,
            fg_color="#222B3A",
            corner_radius=15
        )

<<<<<<< HEAD

        # ====================================================
        # LOAD REPORT
        # ====================================================

        self.latest_report = None

        self.load_latest_report()

    # ====================================================
    # LOAD LATEST REPORT
    # ====================================================

    def load_latest_report(self):
=======
        card.grid(
            row=row,
            column=column,
            sticky="nsew",
            padx=15,
            pady=15
        )

        ctk.CTkLabel(
            card,
            text=name,
            font=("Segoe UI", 13)
        ).pack(
            pady=(15, 5)
        )
>>>>>>> 151acb891a5b5ca9cf0a51ae8c9855e06d790cdd

        value_label = ctk.CTkLabel(
            card,
            text=value,
            font=("Segoe UI", 24, "bold")
        )

        value_label.pack(
            pady=(0, 15)
        )

        self.metric_labels[name] = value_label

    # =================================================

    def update_report(self):

        history = self.dashboard.session_history

        if not history:

<<<<<<< HEAD
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
=======
            return

        # ---------------- BLINKS ----------------

        total_blinks = (
            history[-1].blink_count
        )

        self.metric_labels[
            "Total Blinks"
        ].configure(
            text=str(total_blinks)
        )

        # ---------------- YAWNS ----------------
>>>>>>> 151acb891a5b5ca9cf0a51ae8c9855e06d790cdd

        total_yawns = (
            history[-1].yawn_count
        )

<<<<<<< HEAD
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
=======
        self.metric_labels[
            "Total Yawns"
        ].configure(
            text=str(total_yawns)
        )

        # ---------------- FATIGUE ----------------

        fatigue_values = [

            result.fatigue_score

            for result in history
        ]

        average_fatigue = sum(
            fatigue_values
        ) / len(
            fatigue_values
        )

        self.metric_labels[
            "Average Fatigue"
        ].configure(
            text=f"{average_fatigue:.1f}%"
        )

        # ---------------- DROWSINESS ----------------

        drowsiness_events = 0

        previous_drowsy = False

        for result in history:

            if (
                result.is_drowsy
                and not previous_drowsy
            ):

                drowsiness_events += 1

            previous_drowsy = (
                result.is_drowsy
            )

        self.metric_labels[
            "Drowsiness Events"
        ].configure(
            text=str(
                drowsiness_events
            )
        )

        # ---------------- DISTRACTION ----------------

        distraction_events = 0

        previous_distracted = False

        for result in history:

            if (
                result.is_distracted
                and not previous_distracted
            ):

                distraction_events += 1

            previous_distracted = (
                result.is_distracted
            )

        self.metric_labels[
            "Distraction Events"
        ].configure(
            text=str(
                distraction_events
            )
        )

        # ---------------- EAR ----------------

        ear_values = [

            result.ear

            for result in history
        ]

        average_ear = sum(
            ear_values
        ) / len(
            ear_values
        )

        self.metric_labels[
            "Average EAR"
        ].configure(
            text=f"{average_ear:.3f}"
        )

        # ---------------- MAR ----------------

        mar_values = [

            result.mar

            for result in history
        ]

        average_mar = sum(
            mar_values
        ) / len(
            mar_values
        )

        self.metric_labels[
            "Average MAR"
        ].configure(
            text=f"{average_mar:.3f}"
        )

        # ---------------- RISK ----------------

        if average_fatigue >= 60:

            risk = "HIGH"

        elif average_fatigue >= 30:

            risk = "MEDIUM"

        else:

            risk = "LOW"

        self.metric_labels[
            "Risk Level"
        ].configure(
            text=risk
        )
    def auto_update(self):

        self.update_report()

        self.after(
            1000,
            self.auto_update
        )    
    def generate_report(self):

        history = (
            self.dashboard.session_history
        )

        filepath = (
            self.report_generator.generate_pdf(
                history
            )
        )

        if filepath is None:

            print(
                "⚠️ No session data available"
            )

            return

        print(
            f"✅ PDF report generated:\n"
            f"{filepath}"
        )
>>>>>>> 151acb891a5b5ca9cf0a51ae8c9855e06d790cdd
