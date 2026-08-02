import customtkinter as ctk
from datetime import datetime
from theme import *
import os
from src.reports.report_generator import ReportGenerator

class ReportsPage(ctk.CTkFrame):

    def __init__(self, parent, dashboard):

        super().__init__(
            parent,
            fg_color="transparent"
        )

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

        button_frame.grid(
            row=2,
            column=0,
            pady=(0, 20)
        )

        ctk.CTkButton(
            button_frame,
            text="🔄 Refresh Report",
            command=self.update_report
        ).pack(
            side="left",
            padx=10
        )

        ctk.CTkButton(
            button_frame,
            text="📄 Generate Report",
            command=self.generate_report
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

        print("🔄 Refresh Report clicked")

        history = self.dashboard.session_history

        if not history:

            print(
                "⚠️ No session history available"
            )
            print(
            "📊 History records:",
            len(self.dashboard.session_history)
        )

            self.metric_labels[
                "Total Blinks"
            ].configure(
                text="0"
            )

            self.metric_labels[
                "Total Yawns"
            ].configure(
                text="0"
            )

            self.metric_labels[
                "Average Fatigue"
            ].configure(
                text="0%"
            )

            self.metric_labels[
                "Drowsiness Events"
            ].configure(
                text="0"
            )

            self.metric_labels[
                "Distraction Events"
            ].configure(
                text="0"
            )

            self.metric_labels[
                "Average EAR"
            ].configure(
                text="0.000"
            )

            self.metric_labels[
                "Average MAR"
            ].configure(
                text="0.000"
            )

            self.metric_labels[
                "Risk Level"
            ].configure(
                text="LOW"
            )

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

        total_yawns = (
            history[-1].yawn_count
        )

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
        print(
            "📊 REPORT VALUES:",
            "Blinks =", total_blinks,
            "Yawns =", total_yawns,
            "Fatigue =", round(average_fatigue, 2),
            "Drowsiness =", drowsiness_events,
            "Distraction =", distraction_events,
            "EAR =", round(average_ear, 3),
            "MAR =", round(average_mar, 3)
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